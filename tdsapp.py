{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "49571875",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-08-31 22:43:52.706 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\ProgramData\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the first number: 4\n",
      "Enter the second number: 5\n",
      "Enter the third number: 4\n",
      "The largest number among 4.0 , 5.0 and 4.0 is 5.0\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "st.title(\"largest among 3\")\n",
    "def find_largest(num1, num2, num3):\n",
    "    if num1 >= num2 and num1 >= num3:\n",
    "        largest = num1\n",
    "    elif num2 >= num1 and num2 >= num3:\n",
    "        largest = num2\n",
    "    else:\n",
    "        largest = num3\n",
    "    return largest\n",
    "\n",
    "# Input three numbers from the user\n",
    "num1 = float(input(\"Enter the first number: \"))\n",
    "num2 = float(input(\"Enter the second number: \"))\n",
    "num3 = float(input(\"Enter the third number: \"))\n",
    "\n",
    "largest = find_largest(num1, num2, num3)\n",
    "print(\"The largest number among\", num1, \",\", num2, \"and\", num3, \"is\", largest)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63d4c860",
   "metadata": {},
   "source": [
    "### "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
