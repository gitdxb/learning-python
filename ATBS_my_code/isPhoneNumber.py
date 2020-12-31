{
 "metadata": {
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
   "version": "3.8.5-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python38564bit7e0d748942634174a7df9a61ee12db31",
   "display_name": "Python 3.8.5 64-bit",
   "language": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def isPhoneNumber(text):\n",
    "    if len(text) != 12:\n",
    "        return False\n",
    "    for i in range(0,3):\n",
    "        if not text[i].isdecimal():\n",
    "            return False\n",
    "    if text[3] != '-':\n",
    "        return False\n",
    "    for i in range(4,7):\n",
    "        if not text[i].isdecimal():\n",
    "            return False\n",
    "    if text[7] != '-':\n",
    "        return False\n",
    "    for i in range(8,12):\n",
    "        if not text[i].isdecimal():\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "    print('Is 415-555-4242 a phone number?')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(isPhoneNumber('415-555-4242'))  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Is Moshi moshi a phone number?\nFalse\n"
     ]
    }
   ],
   "source": [
    "print('Is Moshi moshi a phone number?')\n",
    "print(isPhoneNumber('Moshi moshi'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}