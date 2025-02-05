from h2o_wave import Component, ui
from typing import List


def h_gap(size: str) -> Component:
    return ui.text('', width=size)


def v_gap(size: str) -> Component:
    return ui.inline(items=[], height=size)


def list_tile(title: Component,
              subtitle: Component = None,
              leading: Component = None,
              trailing: Component = None) -> Component:
    return ui.inline(
        direction='row',
        justify='between',
        items=[
            ui.inline(
                direction='row',
                align='start',
                justify='center',
                items=[
                    *([leading] if leading else []),
                    ui.inline(
                        direction='column',
                        align='start',
                        justify='center',
                        items=[
                            title,
                            *([subtitle] if subtitle else []),
                        ],
                    ),
                ],
            ),
            *([trailing] if trailing else []),
        ],
    )


def padding(items: List[Component], left: str = '0px', right: str = '0px', top: str = '0px',
            bottom: str = '0px') -> Component:
    return ui.inline(
        items=[
            h_gap(left),
            ui.inline(
                direction='column',
                items=[
                    v_gap(top),
                    *items,
                    v_gap(bottom),
                ],
            ),
            h_gap(right),
        ],
    )
