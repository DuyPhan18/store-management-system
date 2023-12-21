from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from .forms import UpdateUserForm
# Create your views here.
def user_list(request):
    Users = User.objects.filter()
    context = {'Users': Users}
    return render(request, 'user/user.html', context)
def user_info(request, id):
    user_info = get_object_or_404(User, pk = id)
    return render(request, 'user/user_info.html', {'user_info': user_info})

def update_user(request, id):
    user_info = get_object_or_404(User, pk=id)
    form = UpdateUserForm(request.POST or None, instance=user_info)
    if request.method == "POST":
        print("okk")
        print( form.is_valid())
        print( form.errors)
        if form.is_valid():
            # Kiểm tra xác nhận mật khẩu
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 and password2 and password1 != password2:
                form.add_error('password2', "Passwords do not match")
            else:
                # Lưu thông tin người dùng nếu mật khẩu hợp lệ
                form.save()
                return HttpResponseRedirect(reverse('user_info', args=[id]))

    
    return render(request, 'user/user_info.html', {'form': form, 'user_info': user_info})

def delete_user(request, id):
    user = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        # Xác nhận người dùng đã xác nhận xóa
        print(f"Đang xóa người dùng với ID: {user.id}")
        user.delete()
        print(f"Người dùng với ID {user.id} đã được xóa")
        return redirect('/user')

    # Hiển thị trang xác nhận xóa
    return render(request, 'user/user.html', {'user': user})
