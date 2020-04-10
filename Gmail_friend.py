from gmail import GMail, Message

def display_title_bar():
    print('\n *** 与阳间的朋友们传话系统 ***\n\n')

if __name__ == '__main__':
    display_title_bar()
    subject = input('Subject:')
    message = input('Message:')

    gmail = GMail(
        username = 'yz.huang1218@gmail.com',
        password = 'Aa941218**'
    )
    with open('friends.txt','r') as f:
        for friend in f:
            name = friend.split('s')[0].strip().title()
            email = friend.split(',')[1].strip()
            msg = Message(subject='{} {}'.format(subject, name),
                          sender=gmail.username,
                          to=email,
                          text=message)
            print('Sending email to {}'.format(name))
            gmail.send(msg)
    print('Done')