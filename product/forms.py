from django import forms

from product.models import Product, Category, Review


class ProductCreateForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        min_length=3,
        label='Название продукта',
    )
    text = forms.CharField(
        widget=forms.Textarea,
        label='Текст продукта',
        required=False,
    )
    image = forms.ImageField(
        required=False,
        label='Картинка',
    )
    grade = forms.IntegerField(
        label='Оценка',
        required=False,
    )

    def clean_title(self):
        title = self.cleaned_data['title']

        if 'python' not in title.lower():
            raise forms.ValidationError('В заголовке должно быть слово "python"')

        return title


class ProductCreateForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'text', 'image', 'grade')
        labels = {
            'title': 'Название продукта',
            'text': 'Текст продукта',
            'image': 'Картинка',
            'grade': 'Оценка',
        }
        help_texts = {
            'title': 'Введите название продукта',
            'text': 'Введите текст продукта',
            'image': 'Загрузите картинку',
            'grade': 'Введите Оценку',
        }


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = 'text',
        labels = {
            'text': 'Текст категорий',
        }
        help_texts = {
            'text': 'Введите текст категорий',
        }


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = 'text',
        labels = {
            'text': 'напишите что нибудь',
        }
