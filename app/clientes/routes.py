from flask import render_template, redirect,flash
from .forms import NewClient, EditClient
from . import cliente
import app 

@cliente.route("/listar")
def listar():
    clientes = app.models.Cliente.query.all()
    print(clientes)
    return  render_template("TableClient.html", clientes = clientes)
    

@cliente.route("/nuevo", methods = ["GET", "POST"])
def nuevo():
    form = NewClient()
    p = app.models.Cliente()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()

        flash("Cliente registrado correctamente")
        return redirect("/clientes/listar")
    
    return render_template("RegisterClient.html", operacion = "Agregar",  form=form)


@cliente.route("/editar/<id>", methods = ["GET", "POST"])
def Edit(id):
    p = app.models.Cliente.query.get(id)
    form = EditClient(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Cliente actualizado correctamente")
        return redirect("/clientes/listar")
    return render_template("RegisterClient.html", operacion = "Actualizar", form = form)

@cliente.route("/eliminar/<id>")
def Delete(id):
    p = app.models.Cliente.query.get(id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Cliente eliminado correctamente")
    return redirect("/clientes/listar")