# Program Name: Movie Trailer Website
# Module Name: entertainment_center
# Programmer: Jon Tudor
# Purpose: This module provides movie data that is then used via the
# media.Movie class to create the Movie Trailer Website.
import fresh_tomatoes
import media

# Provide data needed to display movies on the Movie Trailer Website
monty_python = media.Movie("Monty Python",
                           "A king goes on a quest to find the Holy Grail",
                           "http://ecx.images-amazon.com/images/I/91wtzn69sGL._SY606_.jpg",
                           "https://www.youtube.com/watch?v=hKNDml12Big")

cloud_atlas = media.Movie("Cloud Atlas",
                          "A connection between two souls over six lifetimes",
                          "http://cdn.wegotthiscovered.com/wp-content/uploads/cloud-atlas-poster.jpg",
                          "https://www.youtube.com/watch?v=ByehYal_cCs")

django = media.Movie("Django",
                     "A man gets retribution and freedom",
                     "http://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                     "https://www.youtube.com/watch?v=eUdM9vrCbow")

space_jam = media.Movie("Space Jam",
                        "Michael Jordan kicks alien butt " +
                        "in basketball with the Looney Toons",
                        "http://assets.nydailynews.com/polopoly_fs/1.1678204!/img/httpImage/image.jpg_gen/derivatives/article_970/article-spacejamweb-0221.jpg",
                        "https://www.youtube.com/watch?v=xMOE5OVwWDE")

the_hangover = media.Movie("The Hangover",
                           "Four guys on a trip to Las Vegas " +
                           "for the bachelor party of a lifetime ",
                           "http://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                           "https://www.youtube.com/watch?v=tcdUhdOlz9M")

the_lego_movie = media.Movie("The Lego Movie",
                             "An adventure in the world of Lego",
                             "http://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
                             "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

# Pass the required movie data values to the movie class to be displayed.
movies = [monty_python, cloud_atlas, django,
    space_jam, the_hangover, the_lego_movie]
fresh_tomatoes.open_movies_page(movies)
