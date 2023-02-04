# Draw these two vectors
# to show that they are orthogonal. Prove their orthogonality using computations.
# Use function draw_vector defined above or create your own better version if you like.
def vector_dot(vec1, vec2):
    """
    Dot product of two vectors
    """

    assert len(vec1) == len(vec2)

    tmp = [v1 * v2 for v1, v2 in zip(vec1, vec2)]
    return sum(tmp)

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



import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 5))

ax.set_xlim([-1.5, 4])
ax.set_ylim([-1.5, 4])

ax.set_xlabel('$x_0$')
ax.set_ylabel('$x_1$')

vec1 = [0.9, 0.2]
vec2 = [-0.3, 1.4]

dot = vector_dot(vec1, vec2)
print(f"(vec1, vec2) = {dot}")

draw_vector(ax, r'$\vec v_1$', 'C0', vec1, orig=[0, 0])
draw_vector(ax, r'$\vec v_2$', 'C1', vec2, orig=[0, 0])

ax.grid()
plt.show()