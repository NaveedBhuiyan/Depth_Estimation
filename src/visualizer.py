import matplotlib.pyplot as plt


class Visualizer:
    @staticmethod
    def visualize_depth_map(depth_map, save_path=None):
        depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min())

        plt.imshow(depth_map, cmap='jet')
        plt.colorbar()
        plt.title('Depth Map')
        plt.axis('off')

        if save_path:
            plt.savefig(save_path)
            print(f"Saved depth map to: {save_path}")
        else:
            plt.show()

        plt.close()
