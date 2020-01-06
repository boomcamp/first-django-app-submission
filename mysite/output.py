import django
django.setup()
from polls.models import Choice, Question 
from django.utils import timezone 
import datetime 
 
# print(Question.objects.all())
# print(Question.objects.filter(id=1))
# print(Question.objects.filter(question_text__startswith='What'))

# # Make sure our custom method worked.
# current_year = timezone.now().year
# print(Question.objects.get(pub_date__year=current_year))

# q = Question.objects.get(pk=1)
# print(q.was_published_recently())
# #True
# print(q.choice_set.all())
# #<QuerySet []>

# # #Create Tgree Choices
# # q.choice_set.create(choice_text='Not much', votes=0)
# # # <Choice: Not much>
# # q.choice_set.create(choice_text='The sky', votes=0)
# # # <Choice: The sky>
# # c=q.choice_set.create(choice_text='Just hacking again', votes=0)

# # print(c.question)

# print(q.choice_set.count())
# # <Choice: Just hacking again>
# c = q.choice_set.filter(choice_text__startswith='The sky')
# c.delete()



future_question = Question(pub_date=timezone.now()+datetime.timedelta(days=30))
print(future_question.was_published_recently())
#False

from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client  
client = Client()

response = client.get('/')
response.status_code
# print(response.status_code)
#Invalid HTTP_HOST header: 'testserver'. You may need to add 'testserver' to ALLOWED_HOSTS.
#Bad Request: /
#400

from django.urls import reverse  

response = client.get(reverse('polls:index'))
response.status_code
  
print(response.context['latest_question_list'])