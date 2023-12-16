First Steps
=====

Simple example
--------------

The simples NavCLI applications looks like this:

.. code-block:: python

    import curses

    from navcli.navigation import Navigation
    from navcli.structs import Option, View
    from navcli.actions import QUIT, Redirect

    another_view = View(
        title='Another View',
        options=[
            Option(label='Done', action=QUIT),
            Option(label='Exit', action=QUIT),
        ]
    )

    main_view = View(
        title='Main Menu',
        options=[
            Option(label='Go to another view', action=Redirect(another_view)),
            Option(label='Exit', action=QUIT),
        ]
    )

    def main(stdscr):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        navigation = Navigation(stdscr, main_view)
        navigation.navigate()


    def run():
        curses.wrapper(main)

    if __name__ == '__main__':
        run()


Explanation
----------

Let's break it down:

.. code-block:: python

    import curses

    from navcli.navigation import Navigation
    from navcli.structs import Option, View
    from navcli.actions import QUIT, Redirect

First we import the necessary modules. The ``curses`` module is used to
render the UI. 
The ``Navigation`` class is the main class of the library.
The ``Option`` and ``View`` classes are used to define the UI.
The ``QUIT`` and ``Redirect`` classes are used to define actions.

.. code-block:: python

    another_view = View(
        title='Another View',
        options=[
            Option(label='Done', action=QUIT),
            Option(label='Exit', action=QUIT),
        ]
    )

    main_view = View(
        title='Main Menu',
        options=[
            Option(label='Go to another view', action=Redirect(another_view)),
            Option(label='Exit', action=QUIT),
        ]
    )

Here we define two views. The ``main_view`` is the main view of the application.
The ``another_view`` is a view that can be reached from the ``main_view``.
The ``main_view`` has two options: ``Go to another view`` and ``Exit``.
The ``Go to another view`` option has an action that redirects to the
``another_view``. The ``Exit`` option has an action that quits the application.

.. code-block:: python

    def main(stdscr):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        navigation = Navigation(stdscr, main_view)
        navigation.navigate()


    def run():
        curses.wrapper(main)

    if __name__ == '__main__':
        run()

Here we define the ``main`` function that is the entry point of the application.
The ``main`` function is wrapped by the ``curses.wrapper`` function.
The ``main`` function initializes the ``Navigation`` class with the ``main_view``
and calls the ``navigate`` method of the ``Navigation`` class.

The ``run`` function is used to run the ``main`` function.

The ``if __name__ == '__main__':`` block is used to run the ``run`` function
if the script is executed directly.

The ``curses.curs_set(0)`` line is used to hide the cursor.
The ``curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)`` line is used
to define the color pair that is used to render the UI.

The ``navigation.navigate()`` line is used to start the navigation.

The ``navigation.navigate()`` method is a blocking method. It returns when the
``QUIT`` action is executed.

The ``navigation.navigate()`` method can be called multiple times. It is not
necessary to create a new ``Navigation`` instance for each navigation.