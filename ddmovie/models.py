from django.db import models
from django_mysql.models import JSONField
from rest_framework import serializers


class MoviePeople(models.Model):

    class Meta:
        verbose_name = '艺人'
        verbose_name_plural = '艺人'

    _id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    name = models.CharField(max_length=64, verbose_name="姓名", unique=False, db_index=True)
    image = models.ImageField(verbose_name="图片", upload_to='movie/peoples/', null=True)
    speciality = models.CharField(max_length=128, verbose_name="职业", default="")
    nationality = models.CharField(max_length=128, verbose_name="国籍", default="")
    raw = JSONField(verbose_name="元数据", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    @property
    def first_image_path(self):
        if self.image:
            return self.image.url
        elif self.raw and self.raw.get('photoOfPerson'):
            photoOfPerson = self.raw['photoOfPerson']
            if photoOfPerson and len(photoOfPerson) > 0:
                return photoOfPerson[0].get('imagePath')
        else:
            moviePhotos = MoviePhoto.objects.get(movieUri=self.uri)
            if moviePhotos:
                return moviePhotos.image.url
        return


class Movie(models.Model):

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = '电影'

    class PeopleSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = MoviePeople
            fields = [
                '_id',
                'name',
                'speciality',
                'nationality',
                'uri',
                # 'raw',
                'first_image_path',
            ]

    _id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    name = models.CharField(max_length=64, verbose_name="电影名", unique=False, db_index=True)
    image = models.ImageField(verbose_name="图片", upload_to='movie/movies/', null=True)
    pub_date = models.CharField(max_length=32, verbose_name="发布时间", default="")
    movie_type = models.CharField(max_length=128, verbose_name="类型", default="")
    raw = JSONField(verbose_name="元数据", null=True)
    detail_raw = JSONField(verbose_name="详细信息元数据", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    @property
    def first_image_path(self):
        if self.image:
            return self.image.url
        else:
            moviePhotos = MoviePhoto.objects.get(movieUri=self.uri)
            if moviePhotos:
                return moviePhotos.image.url
            return


    @property
    def directors(self):
        if not self.raw:
            return []
        directors_raw = self.raw.get('directorList')
        director_list = []
        if directors_raw and len(directors_raw) > 0:
            for director_raw in directors_raw:
                director = MoviePeople.objects.get(uri=director_raw.get('puri'))
                if director:
                    director_list.append(Movie.PeopleSerializer(director).data)
        return director_list

    @property
    def actors(self):
        if not self.raw:
            return []
        actors_raw = self.raw.get('actorList')
        actor_list = []
        if actors_raw and len(actors_raw) > 0:
            for actor_raw in actors_raw:
                actor = MoviePeople.objects.get(uri=actor_raw.get('puri'))
                if actor:
                    actor_list.append(Movie.PeopleSerializer(actor).data)
        return actor_list


class MoviePhoto(models.Model):

    class Meta:
        verbose_name = '电影照片'
        verbose_name_plural = '电影照片'

    _id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    raw = JSONField(verbose_name="元数据", null=True)
    photoType = models.CharField(max_length=64, null=True, default=None)
    movieName = models.CharField(max_length=128, verbose_name="电影名称",null=True)
    movieUri = models.CharField(max_length=128, verbose_name="电影URI",null=True, default=None)
    cinemaName = models.CharField(max_length=128, verbose_name="影院名称",null=True)
    cinemaUri = models.CharField(max_length=128, verbose_name="影院URI",null=True, default=None)
    photo_date = models.DateField(verbose_name="日期", null=True)
    image = models.ImageField(verbose_name="图片", upload_to='movie/photos/', null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")


class MoviePhotoPeople(models.Model):

    class Meta:
        verbose_name = '照片人物关系'
        verbose_name_plural = '照片人物关系'
        unique_together = (("photoUri", "peopleUri"),)

    _id = models.AutoField(primary_key=True)
    photoUri = models.CharField(max_length=128, verbose_name="剧照URI", null=False)
    peopleUri = models.CharField(max_length=128, verbose_name="影人URI", null=False)
    peopleName  = models.CharField(max_length=128, verbose_name="影人姓名", null=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")


class MovieCinema(models.Model):

    class Meta:
        verbose_name = '影院'
        verbose_name_plural = '电影院'

    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name="影院名称", unique=True, db_index=True)
    nameEn = models.CharField(max_length=64, verbose_name="英文名")
    image = models.ImageField(verbose_name="图片", upload_to='movie/cinemas/', null=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    architectureUri = models.CharField(max_length=128, verbose_name="建筑URI", unique=False)
    des = models.CharField(max_length=1024, verbose_name="描述")
    raw = JSONField(verbose_name="元数据", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

