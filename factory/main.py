<<<<<<< HEAD
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
print(button)
=======
>>>>>>> 584d5e1e274925fb185be1f786f8d86f545aa3f5
