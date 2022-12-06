---
layout: page
title: Setup
root: .
---

To follow this workshop, you will need three things: an account on Bert,
an SSH client, and the Filezilla application for transferring files.

{% comment %} {% endcomment %}
<div id="scw">
  <h3>Request an account</h3>

  In this workshop we will use Slurm on Bert in order to use High-Performance Computing. For this, you will need an
  account on Bert.

  <ol>
    <li>Visit <a href="https://bioinformatics.ibers.aber.ac.uk/request.html">
    The account request page (while on campus/VPN)</a></li>
	<li>Fill in the form requesting an account.
    Your account request will be processed by an administrator.</li>
	<li>Once you receive an email indicating that your account has been
    created</li>
  </ol>
</div> 

{% comment %} {% endcomment %}
<div id="SSH">
  <h3>SSH</h3>
  
  SSH is used to connect to the Unix shell on machines across the network.

  <div class="row">
    <div class="col-md-4">
      <h4 id="ssh-windows">Windows</h4>
      <ol>
        <li> If you are using Windows and also following the <a href="https://swcarpentry.github.io/shell-novice">Unix Shell</a> lesson,
then the Git Bash tool installed as part of that lesson will provide you with this.</li>
        <li> Otherwise, then download and install <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html">PuTTY</a>.</li>
      </ol>
    </div>
    <div class="col-md-4">
      <h4 id="ssh-mac">macOS</h4>
      <ol>
        <li>SSH is installed as part of macOS and is available via the Terminal application.</li>
      </ol>
    </div>
    <div class="col-md-4">
      <h4 id="ssh-linux">Linux</h4>
      <ol>
        <li>SSH is installed as part of Linux and is available through a terminal/console application.</li>
      </ol>
    </div>
  </div>
</div>
{% comment %} End of 'SSH' section {% endcomment %}


{% comment %} {% endcomment %}
<div id="filezilla">
  <h3>FileZilla</h3>

  We will use FileZilla to transfer files to and from the Supercomputing Wales facilities.

  <div class="row">
    <div class="col-md-4">
      <h4 id="filezilla-windows">Windows</h4>
      <ol>
        <li>Open <a href="https://filezilla-project.org/download.php?platform=win64">https://filezilla-project.org/download.php?platform=win64</a> with your web browser.</li>
	<li>Download and run the installer. You only need FileZilla, not FileZilla Pro.</li>
	<li>Follow the on-screen instructions. Note that while the installer may try to convince you to install additional software, you do not need to agree to this; if you do not agree to the additional license agreement, FileZilla will still install.</li>
      </ol>
    </div>
    <div class="col-md-4">
      <h4 id="filezilla-mac">macOS</h4>
      <ol>
        <li>Open <a href="https://filezilla-project.org/download.php?platform=osx">https://filezilla-project.org/download.php?platform=osx</a> with your web browser.</li>
	<li>Download and open the Client bundle. You only need FileZilla, not FileZilla Pro.</li>
	<li>Copy the FileZilla app to your Applications folder.</li>
      </ol>
    </div>
    <div class="col-md-4">
      <h4 id="filezilla-linux">Linux</h4>
      <ol>
        <li>Search for and install FileZilla in your distribution's package manager.</li>
      </ol>
    </div>
  </div>
</div>
{% comment %} End of 'FileZilla' section {% endcomment %}
