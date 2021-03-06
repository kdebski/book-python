.. _Performance Optimization:

************************
Performance Optimization
************************


PyPy
====
* http://pypy.org
* No GIL
* Can speedup couple order of magnitude


Seven strategies
================
* https://www.youtube.com/watch?v=zQeYx87mfyw
* https://www.youtube.com/watch?v=EEUXKG97YRw

Line Profiling
--------------
* ``pip install line_profiler``

Numpy vectorization
-------------------
.. figure:: img/scipy-ecosystem.png
    :scale: 50%
    :align: center

    Scipy Ecosystem

Specialized data structures
---------------------------
* ``scipy.spatial`` - for spatial queries like distances, nearest neighbours, etc.
* ``pandas`` - for SQL-like grouping and aggregation
* ``xarray`` - for grouping across multiple dimensions
* ``scipy.sparse`` - sparse metrics for 2-dimensional structured data
* ``sparse`` (package) - for N-dimensional structured data
* ``scipy.sparse.csgraph`` - for graph-like problems (e.g. finding shortest paths)

CPython
-------
* types

Numba
-----
Numba gives you the power to speed up your applications with high performance functions written directly in Python. With a few annotations, array-oriented and math-heavy Python code can be just-in-time compiled to native machine instructions, similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters.

Dask
----
Dask natively scales Python. Dask provides advanced parallelism for analytics, enabling performance at scale for the tools you love

Find existing implementation
----------------------------


Use ``set`` instead of ``list``
===============================
Jeżeli masz listę w której sprawdzasz czy element występuje, to zamień listę na ``set``, dzięki temu będzie lepsza złożoność

.. code-block:: python

    NAMES = ['José', 'Иван', 'Max']

    if 'Max' in NAMES:
        pass

.. code-block:: python

    NAMES = {'José', 'Иван', 'Max'}

    if 'Max' in NAMES:
        pass


Use ``list.append()`` instead of ``str + str``
===============================================
.. code-block:: python

    # Performance - Method concatenates strings using + in a loop
    html = '<table>'

    for element in lista:
        html += f'<tr><td>{element}</td></tr>'

    html += '</table>'
    print(html)

.. code-block:: python

    # Problem solved
    html = ['<table>']

    for element in lista:
        html.append(f'<tr><td>{element}</td></tr>')

    html.append('</table>')
    print(''.join(html))


Range between two ``float``
===========================
* Uwaga na set zawierający floaty, bo pomiędzy dwoma wartościami jest nieskończona ilość wyrażeń

.. code-block:: python

    range(0, 2)
    # 0
    # 1

    range(0.0, 2.0)
    # ...

Inne
====
* Jeżeli coś ``collections.deque`` - Double ended Queue
* Serializowanie kolejki przy wielowątkowości


Further Reading
===============
* https://wiki.python.org/moin/TimeComplexity
* https://visualgo.net/bn/sorting
* http://sorting.at/
* https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html


Assignments
===========

Memoization
-----------
#. Skopiuj kod z listingu poniżej
#. Stwórz pusty ``dict`` o nazwie ``CACHE``
#. W słowniku będziemy przechowywali wyniki wyliczenia funkcji dla zadanych parametrów:

    - klucz: argument funkcji
    - wartość: wynik obliczeń

#. Zmodyfikuj funkcję ``factorial_cache(n: int)``
#. Przed uruchomieniem funkcji, sprawdź czy wynik został już wcześniej obliczony:

    - jeżeli tak, to zwraca dane z ``CACHE``
    - jeżeli nie, to oblicza, aktualizuje ``CACHE``, a następnie zwraca wartość

#. Porównaj prędkość działania


:About:
    * Filename: ``performance_memoize.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 15 min

:Hints:
    * ``import timeit`` - :ref:`timeit`
    * .. code-block:: python

        def factorial_nocache(n: int) -> int:
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)

        def factorial_cache(n: int) -> int:
            raise NotImplementedError


        duration_cache = timeit(
            stmt='factorial_cache(500); factorial_cache(400); factorial_cache(450); factorial_cache(350)',
            globals=globals(),
            number=10000,
        )

        duration_nocache = timeit(
            stmt='factorial_nocache(500); factorial_nocache(400); factorial_nocache(450); factorial_nocache(350)',
            globals=globals(),
            number=10000
        )

        print(f'factorial_cache time: {round(duration_cache, 4)} seconds')
        print(f'factorial_nocache time: {round(duration_nocache, 3)} seconds')
        print(f'Cached solution is {round(duration_nocache / duration_cache, 1)} times faster')
