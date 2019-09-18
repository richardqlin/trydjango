from django.shortcuts import render, get_object_or_404


from django.views import View

# Create your views here.

#BASE VIEW Class = VIEW


class CourseView(View):
	template_name = 'courses/course_detail.html'
	def get(self,requestid= None, *arg,**kwargs):
		context = {}
		if id is not None:
			obj = get_object_or_404(Course,id = id)
			context['object']= =obj
		return render (request,self.template_name, context)

'''

def my_fbv(request,*arg,**kwargs):
	return render (request,'about.html',{})
'''
# HTTP


