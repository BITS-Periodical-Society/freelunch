import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelunch.settings')
from sys import exit

import django
django.setup()

import random
from flapp import models

from faker import Faker
fake = Faker()

sections = []
for i in models.Section:
    sections.append(i[0])

author_designations = []
for i in models.Writer_Designation:
    author_designations.append(i[0])

editor_designations = []
for i in models.Editor_Designation:
    editor_designations.append(i[0])

def add_author():
    a = models.Writer.objects.get_or_create(name=fake.name(), bio=fake.text(250), designation=random.choice(author_designations), email=fake.email())[0]
    a.save()
    return a

def add_editor():
    e = models.Editor.objects.get_or_create(name=fake.name(), bio=fake.text(250), designation=random.choice(editor_designations), email=fake.email())[0]
    e.save()
    return e

def add_comment(post):
    c = models.Comment.objects.get_or_create(post=post,author=fake.name(), text=fake.text(), is_approved=fake.boolean())[0]
    c.save()
    return c


def populate():

    a_num = input('Enter the number of authors you want: ')
    e_num = input('Enter the number of editors you want: ')
    p_num = input('Enter the number of posts you want: ')
    c_num = input('Enter the max number of comments per post. Not all comments will be published: ')

    try:
        a_num = int(a_num)
        e_num = int(e_num)
        p_num = int(p_num)
        c_num = int(c_num)

    except:
        print("Please use integers.")
        exit(0)

    print('Faking authors...')
    for i in range(a_num):
        add_author()
    print('Faking editors...')
    for i in range(e_num):
        add_editor()

    print('Adding fake posts...\nMight take some time')
    for newpost in range(p_num):
        # f_author = random.choice(models.Writer.objects.all())
        f_editor = random.choice(models.Editor.objects.all())
        f_title = fake.sentence()
        f_content = fake.paragraph(40)+'\n\n'+fake.paragraph(70)+'\n\n'+fake.paragraph(30)
        f_synop = fake.paragraph(30)
        f_section = random.choice(sections)
        f_cdate = fake.date()
        f_pdate = fake.date()

        post = models.Post.objects.get_or_create(post_editor=f_editor,title=f_title,content=f_content,synopsis=f_synop,section=f_section, created_date=f_cdate, published_date=f_pdate)[0]
        f_auth = random.choice(models.Writer.objects.all())
        post.author.add(f_auth)
        f_auth.posts.add(post)
        if fake.boolean():
            f_auth = random.choice(models.Writer.objects.all())
            post.author.add(f_auth)
            f_auth.posts.add(post)
        post.save()

        for newcomment in range(c_num):
            add_comment(post)

print('Welcome to fake data creation for Freelunch!\nThis script will help you add authors, editors, posts and comments')
print('The added data will have some contradictions regarding dates where the post or comments will be published before it had been created.')
print('But since that does not defeat our purpose, we will ignore it to keeep it simple.')
print('All the posts that are added will be published. It is not true for comments.')
print('Authors and editors already present in th database will also be used')
print('Last but not the least, all posts will have the default cover image. We are working on it.')

print("\nMake sure you have 'Faker 1.0.7' installed. To install dependencies, check README.md")
print('\n')

populate()

print('All done. Go checkout the website. Don\'t forget to run the server!')
