from sqlmodel import Session

from database import engine
from models import Genre, Movie


def create_movie_with_genre():
    with Session(engine) as session:
        try:
            genre = Genre(name="Horror")
            session.add(genre)
            session.flush()

            movie = Movie(
                title="Quietplace", in_theaters=50, release_year=2008, genre_id=genre.id
            )

            session.add(movie)
            session.commit()
        except Exception as error:
            session.rollback()
            print(error)


create_movie_with_genre()
