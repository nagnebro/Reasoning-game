from ursina import *


class Inventory(Entity):
    def __init__(self, player_data, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.015),
            texture='white_cube',
            texture_scale=(4, 6),
            scale=(.4, .6),
            origin=(-.5, .5),
            position=(-.8, .4),
            color=color.color(0, 0, .1, .9),
        )
        for item in player_data.inventory:
            self.append(item)
            print(item.text)

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.screen  = Draggable(enabled = False)


    def find_free_spot(self):
        for y in range(8):
            for x in range(4):
                grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1])) for e in
                                  self.children]
                print(grid_positions)

                if not (x, -y) in grid_positions:
                    print('found free spot:', x, y)
                    return x, y

    def append(self, item, x=0, y=0):
        print('add item:', item)

        if len(self.children) >= 4 * 6:
            print('inventory full')
            error_message = Text('<red>Inventory is full!', origin=(0, -1.5), x=-.5, scale=2)
            destroy(error_message, delay=1)
            return

        x, y = self.find_free_spot()


        icon = Draggable(
            parent=self,
            model='quad',
            texture=item.texture,
            color=color.white,
            desc = item.desc,
            scale_x=1 / self.texture_scale[0],
            scale_y=1 / self.texture_scale[1],
            origin=(-.5, .5),
            x=x * 1 / self.texture_scale[0],
            y=-y * 1 / self.texture_scale[1],
            z=-.5,
        )




        icon.tooltip = Tooltip(item.name)
        icon.tooltip.font = "NanumSquareRoundB.ttf"
        icon.tooltip.background.color = color.color(0, 0, 0, .8)




        def drag():


            icon.org_pos = (icon.x, icon.y)
            icon.z -= .01  # ensure the dragged item overlaps the rest

        def drop():
            icon.x = int((icon.x + (icon.scale_x / 2)) * 4) / 4
            icon.y = int((icon.y - (icon.scale_y / 2)) * 6) / 6
            icon.z += .01

            # if outside, return to original position
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:

                # item은 inventory의 proviso객체를 뜻하고 icon은 그 객체에서 desc, text정도만 넘겨받은 객체
                icon.position = (icon.org_pos)
                print("icon",icon.desc)
                print("icon",icon.texture)

                print('item', item.texture)
                self.parent.append(item)
                print('dropp1')


                return
            else:
                self.open_screen(icon=icon)

            # if the spot is taken, swap positions
            for c in self.children:
                print('dropp2')

                if c == icon:
                    continue

                if c.x == icon.x and c.y == icon.y:
                    print('swap positions')
                    c.position = icon.org_pos

        icon.drag = drag
        icon.drop = drop





    def open_screen(self,icon):


        if self.screen .enabled == False:
            self.screen  = Draggable(
                    parent=camera.ui,
                    model=Quad(radius=.015),
                    texture='white_cube',

                    scale=(1.2, .9),
                    z=-10,

                    color=color.color(0, 0, .1, .9),

                    disabled=True,


            )

            btn = Button(

                parent=camera.ui,
                model='quad',
                scale=(.15, .1),
                radius=1,
                z=-1,
                text='확인',
                color=color.gray,

            )

            img = Entity(
                parent=camera.ui,
                model='quad',
                scale=(.7, .7),
                z=-1,
                texture=icon.texture,
                color=color.white,

            )
            text = Text(text=icon.desc, origin=(0, 0))
            text.font = "NanumSquareRoundR.ttf"

            btn.text_entity.font = "NanumSquareRoundR.ttf"
            # text.text_entity.font = "NanumSquareRoundR.ttf"
            btn.parent = self.screen   # entity요소끼리 서로 부모 자식 관계를 맺어주면 객체끼리 상대적인 포지션을 가지고 붙어다닐 수 있다.
            img.parent = self.screen   # img 요소도 스크린과 묶어놓는다.
            text.parent = self.screen   # 텍스트 박스 생성.
            img.position = (0, 0.15, -1)
            btn.position = (0, -.35, -1)
            text.position = (0, -.2, -1)
            btn.on_click = self.screen.disable




if __name__ == '__main__':
    app = Ursina()
    inventory = Inventory()
    window.borderless = False


    def add_item():
        inventory.append(random.choice(('bag', 'bow_arrow', 'gem', 'orb', 'sword')))


    add_item()
    add_item()
    add_item_button = Button(
        scale=(.1, .1),
        x=-.5,
        color=color.lime.tint(-.25),
        text='+',
        tooltip=Tooltip('Add random item'),
        on_click=add_item
    )
    bg = Entity(parent=camera.ui, model='quad', texture='shore', scale_x=camera.aspect_ratio, z=1)
    Cursor(texture='cursor', scale=.1)
    mouse.visible = False
    window.exit_button.visible = False
    window.fps_counter.enabled = False
    app.run()

