from threading import Lock, Thread


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class EloConstant(metaclass=SingletonMeta):
    # Singleton class for fun, and to practice using singletons
    K: int = 50

    def __init__(self, K: int) -> None:
        self.K = K


RESULT_WIN = "win"
RESULT_LOSS = "loss"
RESULT_DRAW = "draw"

DEFAULT_RATING = 1000

WIN = 1.0
LOSS = 0.0
DRAW = 0.5

RESULT_TO_SCORE = {
    RESULT_WIN: WIN,
    RESULT_DRAW: DRAW,
    RESULT_LOSS: LOSS
}

# Top 100 Chess Players as of Feb, 2025
CHESS_PLAYERS = [
    ['Carlsen, Magnus', 'NOR', '2833'],
    ['Caruana, Fabiano', 'USA', '2803'],
    ['Nakamura, Hikaru', 'USA', '2802'],
    ['Erigaisi Arjun', 'IND', '2801'],
    ['Gukesh D', 'IND', '2777'],
    ['Abdusattorov, Nodirbek', 'UZB', '2766'],
    ['Firouzja, Alireza', 'FRA', '2760'],
    ['Wei, Yi', 'CHN', '2755'],
    ['Nepomniachtchi, Ian', 'RUS', '2754'],
    ['Anand, Viswanathan', 'IND', '2750'],
    ['So, Wesley', 'USA', '2747'],
    ['Aronian, Levon', 'USA', '2745'],
    ['Dominguez Perez, Leinier', 'USA', '2741'],
    ['Praggnanandhaa R', 'IND', '2741'],
    ['Duda, Jan-Krzysztof', 'POL', '2739'],
    ['Le, Quang Liem', 'VIE', '2739'],
    ['Ding, Liren', 'CHN', '2734'],
    ['Niemann, Hans Moke', 'USA', '2734'],
    ['Keymer, Vincent', 'GER', '2731'],
    ['Mamedyarov, Shakhriyar', 'AZE', '2731'],
    ['Aravindh, Chithambaram VR.', 'IND', '2729'],
    ['Vachier-Lagrave, Maxime', 'FRA', '2729'],
    ['Giri, Anish', 'NED', '2728'],
    ['Fedoseev, Vladimir', 'SLO', '2724'],
    ['Vidit, Santosh Gujrathi', 'IND', '2721'],
    ['Rapport, Richard', 'HUN', '2718'],
    ['Topalov, Veselin', 'BUL', '2717'],
    ['Yu, Yangyi', 'CHN', '2715'],
    ['Dubov, Daniil', 'RUS', '2701'],
    ['Wang, Hao', 'CHN', '2701'],
    ['Sindarov, Javokhir', 'UZB', '2700'],
    ['Radjabov, Teimour', 'AZE', '2698'],
    ['Svidler, Peter', 'FID', '2696'],
    ['Esipenko, Andrey', 'FID', '2695'],
    ['Andreikin, Dmitry', 'FID', '2695'],
    ['Harikrishna, Pentala', 'IND', '2695'],
    ['Deac, Bogdan-Daniel', 'ROU', '2692'],
    ['Sevian, Samuel', 'USA', '2692'],
    ['Artemiev, Vladislav', 'RUS', '2691'],
    ['Liang, Awonder', 'USA', '2690'],
    ['Robson, Ray', 'USA', '2689'],
    ['Van Foreest, Jorden', 'NED', '2688'],
    ['Grischuk, Alexander', 'RUS', '2687'],
    ['Nihal Sarin', 'IND', '2687'],
    ['Bu, Xiangzhi', 'CHN', '2684'],
    ['Kasimdzhanov, Rustam', 'UZB', '2681'],
    ['Maghsoodloo, Parham', 'IRI', '2680'],
    ['Navara, David', 'CZE', '2677'],
    ['Sarana, Alexey', 'SRB', '2672'],
    ['Shankland, Sam', 'USA', '2670'],
    ['Vitiugov, Nikita', 'ENG', '2670'],
    ['Vokhidov, Shamsiddin', 'UZB', '2670'],
    ['Anton Guijarro, David', 'ESP', '2668'],
    ['Howell, David W L', 'ENG', '2668'],
    ['Nguyen, Thai Dai Van', 'CZE', '2668'],
    ['Sadhwani, Raunak', 'IND', '2666'],
    ['Tabatabaei, M. Amin', 'IRI', '2666'],
    ['Leko, Peter', 'HUN', '2666'],
    ['Svane, Frederik', 'GER', '2665'],
    ['Adams, Michael', 'ENG', '2664'],
    ['Saric, Ivan', 'CRO', '2661'],
    ['Alekseenko, Kirill', 'AUT', '2661'],
    ['Oparin, Grigoriy', 'USA', '2660'],
    ['Sargsyan, Shant', 'ARM', '2660'],
    ['Gledura, Benjamin', 'HUN', '2659'],
    ['Yakubboev, Nodirbek', 'UZB', '2659'],
    ['Eljanov, Pavel', 'UKR', '2658'],
    ['Christiansen, Johan-Sebastian', 'NOR', '2658'],
    ['Wojtaszek, Radoslaw', 'POL', '2658'],
    ['Murzin, Volodar', 'FID', '2657'],
    ['Mamedov, Rauf', 'AZE', '2656'],
    ['Morozevich, Alexander', 'RUS', '2656'],
    ['Amin, Bassem', 'EGY', '2654'],
    ['Jones, Gawain C B', 'ENG', '2654'],
    ['Yuffa, Daniil', 'ESP', '2654'],
    ['Shevchenko, Kirill', 'ROU', '2653'],
    ['Dardha, Daniel', 'BEL', '2652'],
    ['Karthikeyan, Murali', 'IND', '2651'],
    ['Indjic, Aleksandar', 'SRB', '2650'],
    ['Inarkiev, Ernesto', 'RUS', '2650'],
    ['Gelfand, Boris', 'ISR', '2649'],
    ['Shirov, Alexei', 'ESP', '2648'],
    ['Cheparinov, Ivan', 'BUL', '2646'],
    ['Ma, Qun', 'CHN', '2645'],
    ['Martirosyan, Haik M.', 'ARM', '2645'],
    ['Grandelius, Nils', 'SWE', '2644'],
    ['Bluebaum, Matthias', 'GER', '2643'],
    ['Kollars, Dmitrij', 'GER', '2643'],
    ['Sjugirov, Sanan', 'HUN', '2643'],
    ['Volokitin, Andrei', 'UKR', '2643'],
    ['Malakhov, Vladimir', 'FID', '2642'],
    ['Mendonca, Leon Luke', 'IND', '2641'],
    ['Bjerre, Jonas Buhl', 'DEN', '2640'],
    ['Bacrot, Etienne', 'FRA', '2640'],
    ['Wang, Yue', 'CHN', '2640'],
    ['Warmerdam, Max', 'NED', '2638'],
    ['Vallejo Pons, Francisco', 'ESP', '2638'],
    ['Najer, Evgeniy', 'FID', '2637'],
    ['Melkumyan, Hrant', 'ARM', '2636'],
    ['Puranik, Abhimanyu', 'IND', '2636'],
    ['Xiong, Jeffery', 'USA', '2636']
]
