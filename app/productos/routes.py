from flask import render_template, redirect, flash
from . import productos
import app 
from .forms import NewProduct, EditProduct
import os


@productos.route("/listar")
def List():
    productos = app.models.Producto.query.all()
    print(productos)
    return  render_template("index.html",productos = productos)
    

@productos.route("/nuevo", methods = ["GET", "POST"])
def New():
    form = NewProduct()
    p = app.models.Producto()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename 
        app.db.session.add(p)
        app.db.session.commit()
        file = form.imagen.data
        file.save(os.path.abspath(os.getcwd()+"/app/productos/imagenes/" + form.imagen.data.filename))
        flash("Producto registrado correctamente")
        return redirect("/productos/listar")
    return render_template("new.html", operacion = "Registrar", form=form)


@productos.route("/editar/<id>", methods = ["GET", "POST"])
def Edit(id):
    p = app.models.Producto.query.get(id)
    form = EditProduct(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Producto actualizado correctamente")
        return redirect("/productos/listar")
    return render_template("new.html", operacion = "Actualizar", form = form)

@productos.route("/eliminar/<id>")
def Delete(id):
    p = app.models.Producto.query.get(id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Producto eliminado correctamente")
    return redirect("/productos/listar")