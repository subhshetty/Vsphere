def get_cr_view(self):
        """
        Get a view ref to all vim.ComputeResource managed objects

        """
        return self.get_container_view(
            obj_type=[pyVmomi.vim.ComputeResource]
        )

 def get_network_view(self):
        """
        Get a view ref to all vim.Network managed objects

        """
        return self.get_container_view(
            obj_type=[pyVmomi.vim.Network]
        )
