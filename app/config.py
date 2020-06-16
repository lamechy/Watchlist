class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'


class ProdConfig(Config):
    '''
    Production configuration child class 

    Args:
        Config: the parent class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True