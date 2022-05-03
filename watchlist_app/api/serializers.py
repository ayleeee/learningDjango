## map all the value 
from rest_framework import serializers
from watchlist_app.models import Review, WatchList,StreamPlatform

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude=('watchlist',)
       #fields ="__all__"
       

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    # new extra field 
    #len_name=serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__"
        #fields=['id','name','description']
        # 제외하고 싶은 것만 써도 됨
        #exclude=['id']
    #access to object = access to field's item individually
    # def get_len_name(self,object):
    #     length = len(object.name)
    #     return length

class StreamPlatformSerializer(serializers.ModelSerializer):
    # related_name에 쓴 걸로 해야한다. 
    #watchlist = WatchListSerializer(many=True,read_only=True)
    watchlist=serializers.HyperlinkedRelatedField (
        many=True,
        read_only=True,
        view_name='movie-detail'
    )
    
    class Meta:
        model = StreamPlatform
        fields="__all__"


# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError("Name is too short!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
    
#     def validate(self,data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError("Title and Description can not be same")
#         else:
#             return data
        
    
    # field level 
    # def validate_name(self,value):
        
    #     if len(value) < 2: 
    #         raise serializers.ValidationError("name is too short!");
    #     else :
    #         return value