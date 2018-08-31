# -*- coding: utf-8 -*-

import boto.sqs


class AmazonSQS(object):
    def __init__(self):
        self.conn = boto.sqs.connect_to_region("us-west-2",
                                      aws_access_key_id='AKIAJQ2WOLF733K3LKGA',
                                      aws_secret_access_key='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')
        print(self.conn)

    def create_queue(self):
        queue = self.conn.create_queue("queue_name")

    def list_all_queues(self):
        for q in self.conn.get_all_queues():
            print(q)

    def get_one_queue(self):
        q = self.conn.get_queue("queue_name")
        print(q)

    def read_msg(self):
        queue = self.conn.get_queue("queue_name")

        msgs = queue.get_messages()
        # msgs = queue.get_messages(visibility_timeout=60)

        if len(msgs) > 0:
            # delete a msg
            queue.delete_message(msgs[0])

        # delete the queue
        self.delete_queue(queue)

    def write_msg(self):
        queue = self.conn.get_queue("queue_name")

        msg = boto.sqs.message()
        msg.set_body("This is a queue msg")

        queue.write(msg)

        msg2 = boto.sqs.message()
        msg2.message_attributes = {
            "name" : "a Name",
            "values" : {
                "data" : "data content",
                "type" : "data type"
            }
        }


    def run(self):
        self.list_all_queues()

        print("Amazon SQS test end")


if __name__ == "__main__":
    sqs = AmazonSQS()
    sqs.run()

