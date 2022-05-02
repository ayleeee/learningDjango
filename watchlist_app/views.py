#from django.shortcuts import render
#from watchlist_app.models import Movie
#from django.http import JsonResponse

#def movie_list(request):
    #movies = Movie.objects.all() ## all the objects that are availiable
    #data={
        #'movies':list(movies.values())
       # }
    
    ## JsonResponse will convert python-dictionary to JSON format
    #return JsonResponse(data)
    
    

#def movie_details(request,pk):
    #movie = Movie.objects.get(pk=pk)
    #data={
     #   'name':movie.name,
      #  'description':movie.description,
       # 'active': movie.active,
    }
    #print(movie.name)
 #   return JsonResponse(data)