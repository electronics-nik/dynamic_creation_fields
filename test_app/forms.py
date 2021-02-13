from django import forms


class MyForm1(forms.Form):
    question = forms.CharField()
    is_active = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    single_answer = forms.BooleanField(widget=forms.CheckboxInput, required=False)

    answer_block_count = forms.CharField(widget=forms.HiddenInput())
    answer_list = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        answers_cnt = kwargs.pop('answers_cnt', 0)

        if len(args):
            answer_list = args[0]['answer_list']
            if answer_list:
                answer_list = [int(value) for value in answer_list.split(',')]
        else:
            answer_list = []

        super(MyForm1, self).__init__(*args, **kwargs)
        self.fields['answer_block_count'].initial = answers_cnt
        self.fields['answer_list'].initial = []

        for idx in range(len(answer_list)):
            self.fields['answer_text_{index}'.format(index=answer_list[idx])] = forms.CharField()
            self.fields['answer_is_active_{index}'.format(index=answer_list[idx])] = forms.BooleanField(
                widget=forms.CheckboxInput(),
                required=False
            )

            self.fields['answer_is_correct_{index}'.format(index=answer_list[idx])] = forms.BooleanField(
                widget=forms.CheckboxInput(),
                required=False
            )

    # def clean(self):
    #     print('clean')
    #
    # def save(self):
    #     print('save')
