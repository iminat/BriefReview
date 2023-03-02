# Draw these three vectors to demonstrate that their sum is zero.
# Use function draw_vector defined above or create your own better version if you like.
def vector_add(vec1, vec2):
    """
    Vector addition vec1 + vec2
    """
    assert len(vec1) == len(vec2)  # lengths must be identical

    return [v1 + v2 for v1, v2 in zip(vec1, vec2)]
def draw_vector(ax, label, color, vec, orig):
    """
    Draw a vector
    -------------
    ax : axes
        The axes to draw
    label : str
        The label of the vector
    color : str
        Color specification
    vec : list of two comopnents
        The vector - shifts dx and dy from orig
    orig : list of two components
        The vector beginning point
    """

    vec_end = [orig[0] + vec[0], orig[1] + vec[1]]
    ax.annotate("",
                xytext=orig,  # arrow beginning point
                xy=vec_end,  # arrow end point
                arrowprops={'color': color});

    # Draw a transparent circle around a label to improve visibility
    bbox = {'facecolor': 'w',
            'edgecolor': 'w',
            'boxstyle': 'circle',
            'alpha': 0.8}

    # Add a text in the middle of the arrow
    ax.text(orig[0] + 0.5 * vec[0], orig[1] + 0.5 * vec[1], label,
            fontsize=16, bbox=bbox, va='center', ha='center')

vec1 = [0.98480775, 0.17364818]
vec2 = [-0.64278761, 0.76604444]
vec3 = [-0.34202014,-0.93969262]
# try to add vec1 and vec2
try:
    vec_sum_12 = vector_add(vec1, vec2)
    print(f"vec_sum_12={vec_sum_12}")
except AssertionError:
    print("Dimensions are incompatible")
# try to add vec1 and vec3 - will fail
try:
    vec_sum_13 = vector_add(vec1, vec3)
    print(f"vec_sum_13={vec_sum_13}")
except AssertionError:
    print("Dimensions are incompatible")


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5,5))

ax.set_xlim([-0.5, 5])
ax.set_ylim([-0.5, 5])

ax.set_xlabel('$x_0$')
ax.set_ylabel('$x_1$')

vec1 = [3.0, 4.0]
vec2 = [1.5, -1.5]
vec_sum = vector_add(vec1, vec2)

draw_vector(ax, r'$\vec v_1$', 'C0', vec1, orig=[0, 0])
draw_vector(ax, r'$\vec v_2$', 'C1', vec2, orig=vec1)
draw_vector(ax, r'$\vec v_1+\vec v_2}$', 'C2', vec_sum, orig=[0, 0])

ax.grid()
plt.show()


