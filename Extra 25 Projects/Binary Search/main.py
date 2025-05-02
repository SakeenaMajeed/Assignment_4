

import streamlit as st
import random
import time

st.set_page_config(page_title="HG Search Algorithm Visualizer", layout="centered")
st.title("🔍 Naive vs Binary Search Performance Checker")

st.markdown("---")

st.markdown("""
Welcome! This tool compares the performance of two search algorithms — **Naive Search** and **Binary Search** — on a randomly generated list.

Naive Search checks each element one-by-one.  
Binary Search uses a divide-and-conquer strategy to find elements faster in a sorted list.

Select the list size and a number to search. Let's see which one wins! 🚀
""")

length = st.slider("📏 Choose list size", min_value=10, max_value=10000, value=10, step=10)
target = st.number_input("🎯 Enter the number you want to search for", value=2)

try:
    sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length - 1) + [target])
except ValueError as e:
    st.error(f"⚠️ Error generating list: {e}")
    st.stop()

def naive_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if st.button("🔍 Start Search", type="primary"):
    iteration = 1000

    start_time = time.perf_counter()
    for _ in range(iteration):
        binary_result = binary_search(sorted_list, target)
    binary_time = (time.perf_counter() - start_time) / iteration

    start_time = time.perf_counter()
    for _ in range(iteration):
        naive_result = naive_search(sorted_list, target)
    naive_time = (time.perf_counter() - start_time) / iteration

    st.markdown("### 📊 Search Results")
    st.write(f"**Naive Search Index:** `{naive_result}`  ⏱️ `{naive_time:.10f}` seconds")
    st.write(f"**Binary Search Index:** `{binary_result}`  ⏱️ `{binary_time:.10f}` seconds")

    st.markdown("### ⚖️ Performance Comparison")
    st.write(f"🔸 Naive Search took `{naive_time:.10f}` seconds on average.")
    st.write(f"🔹 Binary Search took `{binary_time:.10f}` seconds on average.")

    if binary_time < naive_time:
        st.success("🚀 Binary Search is faster and more efficient on sorted lists!")
    else:
        st.info("ℹ️ Both searches performed similarly due to small list size.")

st.markdown("---")
st.caption("🔧 Built with love by **Sakeena Majeed** – Exploring the power of algorithms!")
