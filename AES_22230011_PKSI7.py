{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "820e6de8-884a-4f74-b3ab-36f17f8cc5d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Plaintext asli   : Sabbe Satta Bhavantu Sukhitatta\n",
      "Ciphertext       : 4e9cd4cc9ebdf51c8787f82bd6fb16b1c3b31a97476d43d48616fe0861eea4c4\n",
      "Hasil dekripsi   : Sabbe Satta Bhavantu Sukhitatta\n"
     ]
    }
   ],
   "source": [
    "from Crypto.Cipher import AES\n",
    "from Crypto.Util.Padding import pad, unpad\n",
    "from Crypto.Random import get_random_bytes\n",
    "\n",
    "\n",
    "plaintext = \"Sabbe Satta Bhavantu Sukhitatta\"\n",
    "key = b'agustinusjahakak' \n",
    "\n",
    "\n",
    "data = plaintext.encode('utf-8')\n",
    "data_padded = pad(data, AES.block_size)\n",
    "\n",
    "\n",
    "cipher = AES.new(key, AES.MODE_ECB)  \n",
    "ciphertext = cipher.encrypt(data_padded)\n",
    "\n",
    "\n",
    "cipher_dec = AES.new(key, AES.MODE_ECB)\n",
    "decrypted = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)\n",
    "\n",
    "\n",
    "print(\"Plaintext asli   :\", plaintext)\n",
    "print(\"Ciphertext       :\", ciphertext.hex())\n",
    "print(\"Hasil dekripsi   :\", decrypted.decode('utf-8'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c22b6ce2-23ab-44e4-b9bd-26114b7b121d",
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
