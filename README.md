# README.md



![image-20200926181437930](README.assets/image-20200926181437930.png)



왜 에러뜨지ㅣㅣㅣㅣㅣ

```
위의 오류는 UserCreationForm은 auth.User에서 사용하는 폼이며, 저는 User모델을 커스텀해서 사용했기 때문에,
from .models import User
class SignupForm(UserCreationForm):
   class Meta(UserCreationForm.Meta):
       model = User
       fields = ['username', 'email', 'first_name', 'last_name']
커스텀한 models.py의 User 모델을 직접 가지고와서 Meta 클래스안에 model로 지정해주셔야 합니다~~

```

```
This is a common problem with changing the User mid-way through a project. Common recommendation is to always create a custom User at the beginning of every project, even if it's the same as AbstractUser. That way if you ever need to add/modify the User in the future you don't run into this.
```







![image-20200927164834470](README.assets/image-20200927164834470.png)

```
NoReverseMatch at /accounts/logout/
Reverse for '<WSGIRequest: POST '/accounts/logout/'>' not found. '<WSGIRequest: POST '/accounts/logout/'>' is not a valid view function or pattern name.
```

```
실수로 redirect에 request라는 argument를 넣었따 ㅡㅡ
```



![image-20200927165935793](README.assets/image-20200927165935793.png)

```
textform에서 줄바꿈 허용하는 방법은?!!
```

```
detail.html에서 {{ post.content|linebreaks }} 해주면 끝! 해결!


linebreaks

Replaces line breaks in plain text with appropriate HTML; a single newline becomes an HTML line break (<br />) and a new line followed by a blank line becomes a paragraph break (</p>).

For example:

{{ value|linebreaks }}
If value is Joel\nis a slug, the output will be <p>Joel<br />is a slug</p>.
```

