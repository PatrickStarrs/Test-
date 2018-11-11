{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mom', 'Dad', 'Laura', 'matt', 'Mary', 'Joey', 'Chris', 'Anna', 'Grace']\n"
     ]
    }
   ],
   "source": [
    "family = ['Mom', 'Dad', 'Laura', 'matt', 'Mary', 'Joey', 'Chris', 'Anna', 'Grace']\n",
    "print (family)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Joey\n"
     ]
    }
   ],
   "source": [
    "# Python starts counting at zero, so Joey would be the 5th name in the list\n",
    "print(family [5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Grace\n"
     ]
    }
   ],
   "source": [
    "# the -1 value takes the last element in the list\n",
    "print(family [-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My older brother's name is matt.\n"
     ]
    }
   ],
   "source": [
    "# this script adds the text below and the 3rd person in the family list. the title command would capitalize the m in Matt \n",
    "message = \"My older brother's name is \" + family[3].title() + \".\"\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mother', 'Dad', 'Laura', 'matt', 'Patrick', 'Mary', 'Joey', 'Chris', 'Anna', 'Grace']\n"
     ]
    }
   ],
   "source": [
    "# this changes the first record in the family list. \n",
    "family[0] = 'Mother'\n",
    "print (family)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Joseph', 'Dad', 'Laura', 'matt', 'Mary', 'Joey', 'Chris', 'Anna', 'Grace', 'RileyCooper', 'RileyCooper', 'Riley']\n"
     ]
    }
   ],
   "source": [
    "family.append('Riley')\n",
    "print(family)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Joseph', 'Dad', 'Laura', 'matt', 'Mary', 'Joey', 'Chris', 'Anna', 'Grace', 'Riley']\n"
     ]
    }
   ],
   "source": [
    "family.remove('RileyCooper')\n",
    "print(family)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Joseph', 'Dad', 'Laura', 'matt', 'Patrick', 'Mary', 'Joey', 'Chris', 'Anna', 'Grace', 'Riley']\n"
     ]
    }
   ],
   "source": [
    "# This inserts in the 4 place my name\n",
    "family.insert(4, 'Patrick')\n",
    "print(family)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Joseph', 'Dad', 'Laura', 'matt', 'Patrick', 'Mary', 'Joey', 'Chris', 'Anna', 'Grace']\n"
     ]
    }
   ],
   "source": [
    "del family[10]\n",
    "print(family)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "family.append('Riley')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Joseph', 'Dad', 'Laura', 'matt', 'Patrick', 'Mary', 'Joey', 'Chris', 'Anna', 'Grace', 'Riley']\n"
     ]
    }
   ],
   "source": [
    "print (family)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mother', 'Patrick', 'Mary', 'Joey', 'Chris', 'Anna']\n",
      "Grace\n"
     ]
    }
   ],
   "source": [
    "# the pop function removes the last item in a list, while also allowing you to continue to work with it. \n",
    "popped_family = family.pop()\n",
    "print(family)\n",
    "print (popped_family)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The oldest member of my family is my matt.\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
