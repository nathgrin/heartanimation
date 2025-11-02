

import matplotlib.pyplot as plt
import matplotlib.animation as animation
# plt.rcParams['text.usetex'] = True
import matplotlib
import matplotlib.font_manager as font_manager
import numpy as np
import os

def f(k,x):
    return np.cbrt(np.power(x,2))+0.9*np.sin(k*x)*np.sqrt(3-x*x)
def load_matplotlib_local_fonts(fname):

    # Load a font from TTF file, 
    # relative to this Python module
    # https://stackoverflow.com/a/69016300/315168
    font_path = os.path.join(os.path.dirname(__file__), fname)
    assert os.path.exists(font_path)
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)

    #  Set it as default matplotlib font
    matplotlib.rc('font', family='sans-serif') 
    matplotlib.rcParams.update({
        'font.size': 16,
        'font.sans-serif': prop.get_name(),
    })
def main():
    plt.xkcd()
    load_matplotlib_local_fonts('xkcd-script.ttf')
    """Function Stolen from The Brain Maze"""
    fig = plt.figure(figsize=(3,3)) 
    fig.subplots_adjust(bottom=0.01, top=0.99, left=0.01, right=0.99)

    ax = plt.gca()
    ax.set_xlim(-2,2)
    ax.set_ylim(-1.625,2.375)
    fig.patch.set_facecolor('#ffebf8')
    ax.xaxis.set_ticks_position('none') 
    ax.yaxis.set_ticks_position('none') 
    ax.set_facecolor('#ffebf8')
    x = np.linspace(-2,2,1000000)

    k = 0
    line, = ax.plot(x,f(k,x),c='r',lw=2.)
    text = ax.text(0.99, 0.01, '', ha='right', va='bottom',fontsize=6,transform=ax.transAxes)

    def update(i: int):
        k = np.power(2,i/20.)-1
        line.set_ydata(f(k,x))
        text.set_text(r"$x^{2/3}+0.9\cdot\sin(%.01f x)\cdot\sqrt{3-x^2}$"%k)
        return (line)

    ani = animation.FuncAnimation(fig=fig, func=update, frames=200, interval=60)
    ani.save("hartje.gif",dpi=300)
    plt.show()


if __name__ == "__main__":
    main()