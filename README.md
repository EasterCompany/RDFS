# Rapid Directory & File System

Welcome to the RDFS repository, this is an open-source repository used mostly for storing and distributing publicly
available files.

## Introduction to Overlord

Overlord is a Full Stack Framework for developing Python & TypeScript based multi-platform applications natively on
Android or iOS devices while also being able to deploy the same application to the Web for a great Desktop experience,
you can [Watch a short introductory video here.](https://www.easter.company/overlord/introduction)

### Install Overlord

Download the `create-app` script and run it on your machine

```bash
sudo rm /bin/create-app &>/dev/null
sudo wget -P /bin/ https://raw.githubusercontent.com/EasterCompany/RDFS/Prd/Overlord/create-app
sudo chmod +x /bin/create-app
```

Now whenever you wish to start an Overlord Project simply run the `create-app` command from your terminal.

### Uninstall Overlord

If you wish to remove this script from your system then simply run the following command

```bash
sudo rm /bin/create-app
```

### Install Overlord (Without Sudo)

Once you've run the lines below, you will need to exit your terminal and open it again. Then you will be able to use
the `create-app` command from anywhere on your system.

```bash
rm ~/create-app &>/dev/null
wget -P ~/ https://raw.githubusercontent.com/EasterCompany/RDFS/Prd/Overlord/create-app
mv ~/create-app ~/.create-app
chmod +x ~/.create-app
echo 'alias create-app="~/.create-app"' >> ~/.bashrc
```

### Uninstall Overlord (Without Sudo)

You will also want to remove the `create-app` alias from your `.bashrc` file located at `~/.bashrc`

```bash
rm ~/.create-app
```

For more information you can learn more at [www.easter.company](https://www.easter.company)
