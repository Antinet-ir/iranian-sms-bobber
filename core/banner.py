from pystyle import Colors, Colorate, Center


def show_banner():
    banner = r"""
 █████╗ ███╗   ██╗████████╗██╗███╗   ██╗███████╗████████╗
██╔══██╗████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝╚══██╔══╝
███████║██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗     ██║   
██╔══██║██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝     ██║   
██║  ██║██║ ╚████║   ██║   ██║██║ ╚████║███████╗   ██║   
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   

         💥 Red Team SMS Resilience Tester
         🏴‍☠️ Module-Based | Legal-Only | Iran-Focused
         📁 antinet-ir / sms-bobber-irani
         🧠 t.me/antinet_official

    """
    print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter(banner)))
