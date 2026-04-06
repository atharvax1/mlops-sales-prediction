{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5aa79c59-be74-4b02-8d1a-438a86ce1b0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (fsevents)\n",
      "Traceback (most recent call last):\n",
      "  File \"/opt/anaconda3/lib/python3.13/runpy.py\", line 198, in _run_module_as_main\n",
      "    return _run_code(code, main_globals, None,\n",
      "                     \"__main__\", mod_spec)\n",
      "  File \"/opt/anaconda3/lib/python3.13/runpy.py\", line 88, in _run_code\n",
      "    exec(code, run_globals)\n",
      "    ~~~~^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/opt/anaconda3/lib/python3.13/site-packages/ipykernel_launcher.py\", line 18, in <module>\n",
      "    app.launch_new_instance()\n",
      "    ~~~~~~~~~~~~~~~~~~~~~~~^^\n",
      "  File \"/opt/anaconda3/lib/python3.13/site-packages/traitlets/config/application.py\", line 1074, in launch_instance\n",
      "    app.initialize(argv)\n",
      "    ~~~~~~~~~~~~~~^^^^^^\n",
      "  File \"/opt/anaconda3/lib/python3.13/site-packages/traitlets/config/application.py\", line 118, in inner\n",
      "    return method(app, *args, **kwargs)\n",
      "  File \"/opt/anaconda3/lib/python3.13/site-packages/ipykernel/kernelapp.py\", line 692, in initialize\n",
      "    self.init_sockets()\n",
      "    ~~~~~~~~~~~~~~~~~^^\n",
      "  File \"/opt/anaconda3/lib/python3.13/site-packages/ipykernel/kernelapp.py\", line 331, in init_sockets\n",
      "    self.shell_port = self._bind_socket(self.shell_socket, self.shell_port)\n",
      "                      ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/opt/anaconda3/lib/python3.13/site-packages/ipykernel/kernelapp.py\", line 253, in _bind_socket\n",
      "    return self._try_bind_socket(s, port)\n",
      "           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^\n",
      "  File \"/opt/anaconda3/lib/python3.13/site-packages/ipykernel/kernelapp.py\", line 229, in _try_bind_socket\n",
      "    s.bind(\"tcp://%s:%i\" % (self.ip, port))\n",
      "    ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/opt/anaconda3/lib/python3.13/site-packages/zmq/sugar/socket.py\", line 311, in bind\n",
      "    super().bind(addr)\n",
      "    ~~~~~~~~~~~~^^^^^^\n",
      "  File \"_zmq.py\", line 917, in zmq.backend.cython._zmq.Socket.bind\n",
      "  File \"_zmq.py\", line 179, in zmq.backend.cython._zmq._check_rc\n",
      "zmq.error.ZMQError: Address already in use (addr='tcp://127.0.0.1:49538')\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.13/site-packages/IPython/core/interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import joblib\n",
    "import numpy as np\n",
    "app = Flask(__name__)\n",
    "model = joblib.load(\"model.pkl\")\n",
    "@app.route(\"/predict\", methods=[\"POST\"])\n",
    "def predict():\n",
    "    data = request.json\n",
    "    features = np.array(data[\"features\"]).reshape(1, -1)\n",
    "    \n",
    "    prediction = model.predict(features)\n",
    "    \n",
    "    return jsonify({\"sales_prediction\": prediction.tolist()})\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c60fd9d-bc12-4399-aa75-2f4ebef8a204",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
