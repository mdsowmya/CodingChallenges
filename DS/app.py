from flask import Flask, render_template, request, redirect, url_for
import logging

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/about")
def ind():
    return render_template("about.html")

@app.route('/list', methods=['GET', 'POST'])
def listtext(comments=[]):
    if request.method == "GET":
        return render_template("list.html", comments=comments)
    if request.form.get("insert"):
       comments.append(request.form["text_input"])
    if request.form.get("remove"):
       comments.remove(request.form["text_input"])  
    if request.form.get("clear"):
       comments.clear()
    return redirect(url_for('listtext'))

@app.route('/set', methods=['GET', 'POST'])
def settext(comments=set()):
    if request.method == "GET":
        return render_template("set.html", comments=comments)
    if request.form.get("insert"):
       comments.add(request.form["text_input"])
    if request.form.get("remove"):
       comments.remove(request.form["text_input"])
    if request.form.get("clear"):
       comments.clear()
    return redirect(url_for('settext'))

@app.route('/dictionary', methods=['GET', 'POST'])
def dicttext(comments={}):
    if request.method == "GET":
        return render_template("dict.html", comments=comments)
    if request.form.get("insert"):
       comments.update(eval(request.form["text_input"]))
    if request.form.get("remove"):
       comments.pop(request.form["text_input"])
    if request.form.get("clear"):
       comments.clear()
    return redirect(url_for('dicttext'))

@app.route('/stack', methods=['GET', 'POST'])
def stacktext(comments=[]):
    if request.method == "GET":
        return render_template("stack.html", comments=comments)
    if request.form.get("push"):
       comments.append(request.form["text_input"])
    if request.form.get("pop"):
       if len(comments) != 0:
          comments.pop()
    return redirect(url_for('stacktext'))

@app.route('/queue', methods=['GET', 'POST'])
def queuetext(comments=[]):
    if request.method == "GET":
        return render_template("queue.html", comments=comments)
    if request.form.get("Enqueue"):
       comments.append(request.form["text_input"])
    if request.form.get("Dequeue"):
       if len(comments) != 0:
          comments.pop(0)
    return redirect(url_for('queuetext'))

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

        return new_node.item, new_node.ref

    def search_item(self, x):
        if self.start_node is None:
           return "List has no elements"
        n = self.start_node
        while n is not None:
              if n.item == x:
                 return "Item found"
              n = n.ref
        return "Item not found"

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
           self.start_node = new_node
           return new_node.item, new_node.ref
        n = self.start_node
        while n.ref is not None:
              n = n.ref
        n.ref = new_node;
        return new_node.item, new_node.ref
 
@app.route('/linkedlist', methods=['GET', 'POST'])
def linkedlisttext(comments={}, new_linked_list = LinkedList(), searchitem=[]):
    if request.method == "GET":
        return render_template("linkedlist.html", comments=comments, searchitem=searchitem)
    if request.form.get("insert at start"):
       item, ref = new_linked_list.insert_at_start(request.form["text_input"])
       comments.update({ref:item})
    if request.form.get("insert at end"):
       item, ref = new_linked_list.insert_at_end(request.form["text_input"])
       comments.update({ref:item})
    if request.form.get("search item"):
       result = new_linked_list.search_item(request.form["text_input"])
       searchitem = searchitem.append(result)
    if request.form.get("clear"):
       comments.clear()
        
    return redirect(url_for('linkedlisttext'))

 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
