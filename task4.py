class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = "\t" * level
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

# Приклад використання
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")
reply3 = Comment("Багато негативних відгуків - треба брати!", "Юлія")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)
root_comment.add_reply(reply3)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

reply2_1 = Comment("А мені сподобалось!", "Іван")
reply2.add_reply(reply2_1)
reply2_1_1 = Comment("Ну що там може сподобатись?!?!?", "Марина")
reply2_1.add_reply(reply2_1_1)
reply2_1_2 = Comment("Підтримую!!! Книга гарна! Але не для всіх.", "Петро")
reply2_1.add_reply(reply2_1_2)
reply2_1_2_1 = Comment("Ви на щось натякаєте?", "Марина")
reply2_1_2.add_reply(reply2_1_2_1)

reply3_1 = Comment("Беріть - не пошкодуєте!", "Іван")
reply3.add_reply(reply3_1)

root_comment.display()