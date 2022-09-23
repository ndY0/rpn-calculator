from flask import current_app
from src.services.database import get_database
from src.ops.index import OpsDict

def is_stack(stack_id):
    try:
        conn = get_database(current_app.config['DB_IN_USE'])
        stack_exists = conn.sismember('rdn:stacks', stack_id)
        if(stack_exists == 1):
            return True
        else:
            raise Exception('stack of id {id} does not exists', id=stack_id)
    except Exception as ex:
        raise Exception('cannot get stack : {message}'.format(message=str(ex)))

def create_stack(stack_id):
    try:
        conn = get_database(current_app.config['DB_IN_USE'])
        conn.sadd('rdn:stacks', stack_id)
    except Exception as ex:
        raise Exception('cannot create stack : {message}'.format(message=str(ex)))

def delete_stack(stack_id):
    try:
        is_stack(stack_id)
        conn = get_database(current_app.config['DB_IN_USE'])
        conn.delete('rdn:stacks:{stack_id}'.format(stack_id=stack_id))
        conn.srem('rdn:stacks', stack_id)
    except Exception as ex:
        raise Exception('cannot delete stack : {message}'.format(message=str(ex)))

def push_stack(stack_id, value):
    try:
        is_stack(stack_id)
        conn = get_database(current_app.config['DB_IN_USE'])
        conn.lpush('rdn:stacks:{stack_id}'.format(stack_id=stack_id), value)
    except Exception as ex:
        raise Exception('cannot push to stack : {message}'.format(message=str(ex)))

def pop_stack(stack_id):
    try:
        is_stack(stack_id)
        conn = get_database(current_app.config['DB_IN_USE'])
        return conn.lpop('rdn:stacks:{stack_id}'.format(stack_id=stack_id))
    except Exception as ex:
        raise Exception('cannot pop from stack : {message}'.format(message=str(ex)))

def get_stack(stack_id):
    try:
        is_stack(stack_id)
        conn = get_database(current_app.config['DB_IN_USE'])
        stack_bytes_list = conn.lrange('rdn:stacks:{stack_id}'.format(stack_id=stack_id), 0, -1)
        stack_int_list = list()
        for bytes in stack_bytes_list:
            stack_int_list.append(int(bytes))
        return stack_int_list
    except Exception as ex:
        raise Exception('cannot get stack : {message}'.format(message=str(ex)))

def list_stacks():
    try:
        conn = get_database(current_app.config['DB_IN_USE'])
        stack_bytes_set = conn.smembers('rdn:stacks')
        stack_string_set = set()
        for bytes in stack_bytes_set:
            stack_string_set.add(bytes.decode('utf-8'))
        return stack_string_set
    except Exception as ex:
        raise Exception('cannot get stack : {message}'.format(message=str(ex)))

def length_stack(stack_id):
    try:
        is_stack(stack_id)
        conn = get_database(current_app.config['DB_IN_USE'])
        return conn.llen('rdn:stacks:{stack_id}'.format(stack_id=stack_id))
    except Exception as ex:
        raise Exception('cannot pop from stack : {message}'.format(message=str(ex)))

def check_operand(operand):
    op = OpsDict[operand]
    if(op):
        return op
    else:
        raise Exception('illegal operation : {op}'.format(op=operand))

def apply_operand(operand, stack_id):
    try:
        op = check_operand(operand)
        if(op['value'] == 0):
            stack_length = length_stack(stack_id)
            if(stack_length > 1):
                new_value = int(pop_stack(stack_id)) + int(pop_stack(stack_id))
                push_stack(stack_id, new_value)
            else:
                raise Exception('stack is too small {size} for operation {op}'.format(op=operand, size=stack_length))
        elif(op['value'] == 1):
            stack_length = length_stack(stack_id)
            if(stack_length > 1):
                new_value = int(pop_stack(stack_id)) - int(pop_stack(stack_id))
                push_stack(stack_id, new_value)
            else:
                raise Exception('stack is too small {size} for operation {op}'.format(op=operand, size=stack_length))
        elif(op['value'] == 2):
            stack_length = length_stack(stack_id)
            if(stack_length > 1):
                new_value = int(pop_stack(stack_id)) * int(pop_stack(stack_id))
                push_stack(stack_id, new_value)
            else:
                raise Exception('stack is too small {size} for operation {op}'.format(op=operand, size=stack_length))
        elif(op['value'] == 3):
            stack_length = length_stack(stack_id)
            if(stack_length > 1):
                new_value = int(pop_stack(stack_id)) / int(pop_stack(stack_id))
                push_stack(stack_id, new_value)
            else:
                raise Exception('stack is too small {size} for operation {op}'.format(op=operand, size=stack_length))
        
    except Exception as ex:
        raise Exception('cannot apply op to stack : {message}'.format(message=str(ex)))
