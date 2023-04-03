from tri_selection import tri
from tri_place_test import tableau_aleatoire
import cProfile
import pstats

tab = tableau_aleatoire(5000, - 100, 100)

profiler = cProfile.Profile()
profiler.enable()
tri(tab)
profiler.disable()
profiler.dump_stats("example.stats")


stats = pstats.Stats("example.stats")
stats.print_stats()