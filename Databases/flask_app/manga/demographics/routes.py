from flask import render_template, url_for, redirect, Blueprint, request
from manga.models.demographics import select_Demographics, add_Demographic, delete_Demographic

Demographics = Blueprint('Demographics', __name__)

@Demographics.route('/demographics', methods=['GET'])
def demographics():
    demographics = select_Demographics()
    return render_template('demographics.html', title='Demographics', demographics=demographics)

@Demographics.route('/demographics/add', methods=['POST'])
def add():
    demographic = request.form['demographic']
    add_Demographic(demographic)
    return redirect('/demographics')

@Demographics.route('/demographics/delete', methods=['POST'])
def delete():
    demographic = request.form['demographic']
    delete_Demographic(demographic)
    return redirect('/demographics')