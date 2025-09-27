from js import document


def compute_average(event=None):
    # Get values from the input fields
    s1 = document.getElementById("score1").value
    s2 = document.getElementById("score2").value


    s1 = int(s1) if s1 else 0
    s2 = int(s2) if s2 else 0


    avg = (s1 + s2) / 2


    if avg >= 75:
        document.getElementById("result").innerHTML = f"Average: {avg:.2f} ✅ Passed"
    else:
        document.getElementById("result").innerHTML = f"Average: {avg:.2f} ❌ Failed"

# Attach the function to the button click
document.getElementById("compute").addEventListener("click", compute_average)


