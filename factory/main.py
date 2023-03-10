class IOSButton:
    pass


class AndroidButton:
    pass


class ButtonFactory:
    def create_button(self, os):
        if os == 'ios':
            return f'Button {IOSButton} created'
        else:
            return f'Button {AndroidButton} created'


factory = ButtonFactory()
button = factory.create_button('android')
button = factory.create_button("ios")
button = factory.create_button("android")
print(button)
