from pathlib import Path
import multiprocessing
import subprocess
import click
from loguru import logger
from rich.console import Console
from mydshit.configloader import ConfigurationProvider

console = Console()


def load_config(filepath: str) -> ConfigurationProvider:
	return ConfigurationProvider(filepath)


class DistroBuilder:
	"""Handles the building and configuration of a custom Linux distribution."""
	
	__slots__ = ("base_distro", "config")
	
	def __init__(self, config: ConfigurationProvider) -> None:
		"""Initializes the builder with the selected distribution and optional configuration file."""
		self.config = config
		self.base_distro = self.config.get("base_distro", "arch").lower()
	
	def setup_environment(self) -> None:
		"""Creates the necessary workspace directory for the build process."""
		console.log(f"Setting up environment for {self.base_distro}")
		Path("workspace").mkdir(exist_ok=True, parents=True)
	
	def build_base_system(self) -> None:
		console.log(f"Building base system for {self.base_distro}")
		commands = {
			"arch": ["sudo", "pacstrap", "workspace", "base", "linux", "linux-firmware"],
			"debian": ["sudo", "debootstrap", "stable", "workspace", "http://deb.debian.org/debian"],
			"fedora": ["sudo", "dnf", "install", "--installroot=workspace", "@Core", "-y"],
			"gentoo": ["sudo", "wget", "-O", "workspace/stage3.tar.xz", "https://distfiles.gentoo.org/releases/amd64/autobuilds/latest-stage3-amd64.txt"],
		}
		if self.base_distro in commands:
			process = multiprocessing.Process(target=subprocess.run, args=(commands[self.base_distro],), kwargs={"check": True})
			process.start()
			process.join()
		else:
			logger.error("Unsupported distribution")
	
	def create_iso(self) -> None:
		console.log("Creating ISO image...")
		subprocess.run(["mkisofs", "-o", "output.iso", "workspace"], check=True)


@click.group()
def cli():
	"""
	MYDAK - make your distro aka king
	"""
	pass


@cli.command()
@click.option(
	"--config", help="Configuration output type", required=True
)
def build(config: str):
	config = load_config(config)().get_loaded_config()

	builder = DistroBuilder(config)

	builder.setup_environment()
	builder.build_base_system()

	if config.get("create_iso", True):
		builder.create_iso()


def main():
	cli()


if __name__ == "__main__":
	main()
