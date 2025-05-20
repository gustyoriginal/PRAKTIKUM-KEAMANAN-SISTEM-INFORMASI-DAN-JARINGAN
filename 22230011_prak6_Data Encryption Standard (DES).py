{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b4b8bb22-b5da-4d59-ba2d-4ff41f9ff534",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pycryptodome in c:\\users\\asus\\anaconda3\\lib\\site-packages (3.23.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pycryptodome"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6a21e784-35e3-42a3-a7a0-34e453a4241a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Encrypted: 78fdfd083678960292e9d3355b8ec293806d67d064c8a4bdc6a2d91c30ef8a8c\n",
      "Decrypted: Mataram, mata air kehidupan\n"
     ]
    }
   ],
   "source": [
    "from Crypto.Cipher import DES\n",
    "from Crypto.Random import get_random_bytes\n",
    "from Crypto.Util.Padding import pad, unpad\n",
    "\n",
    "\n",
    "key = b'12345678'\n",
    "\n",
    "\n",
    "cipher = DES.new(key, DES.MODE_ECB)\n",
    "\n",
    "\n",
    "data = b'Mataram, mata air kehidupan'\n",
    "padded_data = pad(data, DES.block_size)  \n",
    "\n",
    "\n",
    "encrypted = cipher.encrypt(padded_data)\n",
    "print(\"Encrypted:\", encrypted.hex())\n",
    "\n",
    "\n",
    "cipher2 = DES.new(key, DES.MODE_ECB)\n",
    "decrypted_padded = cipher2.decrypt(encrypted)\n",
    "decrypted = unpad(decrypted_padded, DES.block_size)\n",
    "print(\"Decrypted:\", decrypted.decode())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b7369b2-162a-4c92-9446-d87861d47abd",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
