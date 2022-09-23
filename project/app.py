from logging import debug
from uuid import uuid1
from flask import Flask, json, request
from src.ops.index import OpsDescriptions
from src.services.stack_services import apply_operand, create_stack, delete_stack, get_stack, list_stacks, push_stack

app = Flask(__name__)
app.config.from_pyfile('src/settings.py')

@app.route("/rpn/op", methods=['GET'])
def get_ops():
    response = app.response_class(
        response=json.dumps(OpsDescriptions),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/rpn/op/<string:op>/stack/<string:stack_id>", methods=['POST'])
def apply_op_to_stack(op, stack_id):
    try:
        apply_operand(op, stack_id)
        return 'OK'
    except Exception as ex:
        response = app.response_class(
            response=str(ex),
            status=400,
            mimetype='plain/text'
        )
        return response

@app.route("/rpn/stack", methods=['POST'])
def create_new_stack():
    try:
        stack_id = str(uuid1())
        create_stack(stack_id)
        response = app.response_class(
            response=json.dumps({"id": stack_id}),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as ex:
        response = app.response_class(
            response=str(ex),
            status=400,
            mimetype='plain/text'
        )
        return response

@app.route("/rpn/stack/<string:stack_id>", methods=['GET'])
def get_stack_by_id(stack_id):
    try:
        stack = get_stack(stack_id)
        response = app.response_class(
            response=json.dumps(stack),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as ex:
        response = app.response_class(
            response=str(ex),
            status=400,
            mimetype='plain/text'
        )
        return response

@app.route("/rpn/stack", methods=['GET'])
def list_all_stacks():
    try:
        stacks = list_stacks()
        response = app.response_class(
            response=json.dumps(list(stacks)),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as ex:
        response = app.response_class(
            response=str(ex),
            status=400,
            mimetype='plain/text'
        )
        return response

@app.route("/rpn/stack/<string:stack_id>", methods=['DELETE'])
def delete_stack_by_id(stack_id):
    try:
        delete_stack(stack_id)
        return 'OK'
    except Exception as ex:
        response = app.response_class(
            response=str(ex),
            status=400,
            mimetype='plain/text'
        )
        return response

@app.route("/rpn/stack/<string:stack_id>", methods=['POST'])
def push_to_stack_by_id(stack_id):
    try:
        content = request.get_json()
        debug(content)
        if(content['value']):
            push_stack(stack_id, content['value'])
            return 'OK'
        else:
            raise Exception('malformed payload')
    except Exception as ex:
        response = app.response_class(
            response=str(ex),
            status=400,
            mimetype='plain/text'
        )
        return response