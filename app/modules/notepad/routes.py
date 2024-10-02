from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from app.modules.notepad.forms import NotepadForm
from app.modules.notepad import notepad_bp
from app.modules.notepad.services import NotepadService

notepad_service = NotepadService()

@notepad_bp.route('/notepad', methods=['GET'])
@login_required
def index():
    form = NotepadForm()
    notepads = notepad_service.get_all_by_user(current_user.id)
    return render_template('notepad/index.html', notepads=notepads, form=form)

'''
CREATE
'''
@notepad_bp.route('/notepad/create', methods=['GET', 'POST'])
@login_required
def create_notepad():
    form = NotepadForm()
    if form.validate_on_submit():
        result = notepad_service.create(title=form.title.data, body=form.body.data, user_id=current_user.id)
        return notepad_service.handle_service_response(
            result=result,
            errors=form.errors,
            success_url_redirect='notepad.index',
            success_msg='Notepad created successfully!',
            error_template='notepad/create.html',
            form=form
        )
    return render_template('notepad/create.html', form=form)


