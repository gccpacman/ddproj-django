from django.db import models
from django.template.defaultfilters import linebreaksbr
from django_mysql.models import JSONField
from rest_framework import serializers
from ddsrc.models import EventRelation, Event

class MoviePeople(models.Model):

    class Meta:
        verbose_name = '影人'
        verbose_name_plural = '影人'

    _id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    name = models.CharField(max_length=64, verbose_name="姓名", unique=False, db_index=True)
    image = models.ImageField(verbose_name="图片", upload_to='movie/peoples/', null=True, blank=True)
    speciality = models.CharField(max_length=128, verbose_name="职业", default="")
    nationality = models.CharField(max_length=128, verbose_name="国籍", default="")
    is_director = models.BooleanField(verbose_name="是否导演", default=False)
    is_actor = models.BooleanField(verbose_name="是否演员", default=False)
    raw = JSONField(verbose_name="元数据", null=True)
    event_count = models.IntegerField(verbose_name='事件个数', default=0)
    screenwriter_count = models.IntegerField(verbose_name='编剧作品个数', default=0)
    director_count = models.IntegerField(verbose_name='导演作品个数', default=0)
    movie_count = models.IntegerField(verbose_name='演出作品个数', default=0)
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
        return

    @property
    def des_html(self):
        if self.raw:
            personDetail = self.raw.get('personDetail')
            if personDetail and len(personDetail) > 0:
                briefBiography = personDetail[0].get('briefBiography')
                if briefBiography and len(briefBiography) > 0:
                    return linebreaksbr(briefBiography[0])
        return

    @property
    def nativeplace(self):
        if self.raw:
            personDetail = self.raw.get('personDetail')
            if personDetail and len(personDetail) > 0:
                return personDetail[0].get('nativePlace', '')
        return
    
    @property
    def nativeplace(self):
        if self.raw:
            personDetail = self.raw.get('personDetail')
            if personDetail and len(personDetail) > 0:
                return personDetail[0].get('nativePlace', None)
        return

    @property
    def birthday(self):
        if self.raw:
            personDetail = self.raw.get('personDetail')
            if personDetail and len(personDetail) > 0:
                return personDetail[0].get('birthday', None)
        return

    @property
    def deathday(self):
        if self.raw:
            personDetail = self.raw.get('personDetail')
            if personDetail and len(personDetail) > 0:
                return personDetail[0].get('deathday', None)
        return

    @property
    def related_movie(self):
        if self.raw:
            movieOfPersons = self.raw.get('movieOfPerson')
            if movieOfPersons and len(movieOfPersons) > 0:
                movie_list = []
                for movieOfPerson in movieOfPersons:
                    movieUri = movieOfPerson['movieUri']
                    movie = Movie.objects.get(uri=movieUri)
                    movie_list.append({
                        '_id': movie._id,
                        'uri': movie.uri,
                        'name': movie.name,
                        'image': movie.first_image_path,
                    })
                return movie_list
        return

    @property
    def related_photo(self):
        if self.raw:
            photoOfPersons = self.raw.get('photoOfPerson')
            if photoOfPersons and len(photoOfPersons) > 0:
                photo_list = []
                for photoOfPerson in photoOfPersons:
                    pUri = photoOfPerson['photoUri']
                    photo = MoviePhoto.objects.get(uri=pUri)
                    photo_list.append({
                        '_id': photo._id,
                        'uri': pUri,
                        'type': photo.photoType,
                        'image': photo.image.url,
                    })
                return photo_list
        return


class MoviePeopleRelation(models.Model):
    class Meta:
        verbose_name = '影人电影关系'
        verbose_name_plural = '影人电影关系'
        unique_together = (("movie_uri", "people_uri"),)

    _id = models.AutoField(primary_key=True)
    movie_uri = models.CharField(max_length=128, verbose_name="电影URI", unique=True)
    people_uri = models.CharField(max_length=128, verbose_name="影人URI", unique=True)
    rule_type = models.CharField(max_length=64, verbose_name="类型", default=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")


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
    des = models.TextField(verbose_name="简介", null=True, blank=True)
    image = models.ImageField(verbose_name="图片", upload_to='movie/movies/', null=True, blank=True)
    lib_image_path = models.URLField(verbose_name="爬取图片", null=True, default=None)
    pub_date = models.CharField(max_length=32, verbose_name="发布时间", default="")
    formated_pub_date = models.IntegerField(verbose_name="格式化的发布时间", default=0)
    movie_type = models.CharField(max_length=128, verbose_name="类型", default="")
    raw = JSONField(verbose_name="元数据", null=True)
    detail_raw = JSONField(verbose_name="详细信息元数据", null=True)
    event_count = models.IntegerField(verbose_name='事件个数', default=0)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    @property
    def first_image_path(self):
        if self.image:
            return self.image
        elif self.lib_image_path:
            return self.lib_image_path
        else:
            moviePhotos = MoviePhoto.objects.filter(movieUri=self.uri)
            if len(moviePhotos) > 0 and moviePhotos[0].image:
                return moviePhotos[0].image.url
            return

    @property
    def des_html(self):
        if not self.des:
            return ''
        return linebreaksbr(self.des)

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
                    director_list.append({
                        '_id': director._id,
                        'name': director.name,
                        'des_html': director.des_html,
                        'image': director.first_image_path
                    })
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
                    actor_list.append({
                        '_id': actor._id,
                        'name': actor.name,
                        'des_html': actor.des_html,
                        'image': actor.first_image_path
                    })
        return actor_list

    @property
    def related_photo(self):
        if self.raw:
            photoOfMovies = MoviePhoto.objects.filter(movieUri=self.uri)
            photo_list = []
            for photoOfMovie in photoOfMovies:
                photo_list.append({
                    '_id': photoOfMovie._id,
                    'uri': photoOfMovie.uri,
                    'type': photoOfMovie.photoType,
                    'image': photoOfMovie.image.url,
                })
                return photo_list
        return


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
    nameEn = models.CharField(max_length=64, verbose_name="英文名", blank=True)
    build_date = models.CharField(max_length=64, verbose_name="建造时间", blank=True)
    image = models.ImageField(verbose_name="图片", upload_to='movie/cinemas/', null=True, blank=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    architectureUri = models.CharField(max_length=128, verbose_name="建筑URI", unique=False)
    longitude = models.FloatField(verbose_name="经度", null=True)
    latitude = models.FloatField(verbose_name="纬度", null=True)
    longitude_bmap = models.FloatField(verbose_name="经度(百度地图)", null=True)
    latitude_bmap = models.FloatField(verbose_name="纬度(百度地图)", null=True)
    des = models.CharField(max_length=1024, verbose_name="描述")
    raw = JSONField(verbose_name="元数据", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    @property
    def first_image_path(self):
        if self.image:
            return self.image.url
        return

    @property
    def des_html(self):
        if self.des:
            return linebreaksbr(self.des)
        return ''

    @property
    def related_people(self):
        people_list = self.raw['personList']
        relate_people_list = []
        for people in people_list:
            puri = people['puri']
            pobj = MoviePeople.objects.get(uri=puri)
            relate_people_list.append({
                '_id': pobj._id,
                'name': pobj.name,
                'des_html': pobj.des_html,
                'first_image_path': pobj.first_image_path
            })
        return relate_people_list

    @property
    def related_event(self):
        event_relation_list = EventRelation.objects.filter(relation_type="place").filter(relation_label=self.name)
        related_event_list = []
        for event_relation in event_relation_list:
            event_uri = event_relation.event_uri
            event = Event.objects.get(uri=event_uri)
            if event:
                related_event_list.append({
                    '_id': event._id,
                    'name': event.event_title,
                    'des_html': event.description,
                    'first_image_path': event.first_image_path,
                    'event_begin': event.event_begin,
                    'event_end': event.event_end,
                })
        return related_event_list