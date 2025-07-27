import React, { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Badge } from "./ui/badge";
import { Button } from "./ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs";
import { Separator } from "./ui/separator";
import { 
  Code, 
  Database, 
  Server, 
  Award, 
  Mail, 
  Phone, 
  Linkedin, 
  Github,
  ExternalLink,
  Calendar,
  MapPin,
  Download
} from "lucide-react";
import { mockData } from "../data/mock";

const Portfolio = () => {
  const [activeSection, setActiveSection] = useState("about");

  const handleDownloadResume = () => {
    // Mock download functionality
    console.log("Downloading resume...");
  };

  return (
    <div className="min-h-screen bg-black text-white">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 z-50 bg-black/90 backdrop-blur-md border-b border-gray-800">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
              Riddhi Kalra
            </div>
            <nav className="hidden md:flex space-x-8">
              {["About", "Projects", "Skills", "Achievements", "Contact"].map((item) => (
                <button
                  key={item}
                  onClick={() => setActiveSection(item.toLowerCase())}
                  className={`px-3 py-2 rounded-lg transition-all duration-300 ${
                    activeSection === item.toLowerCase()
                      ? "bg-blue-600 text-white"
                      : "text-gray-300 hover:text-white hover:bg-gray-800"
                  }`}
                >
                  {item}
                </button>
              ))}
            </nav>
            <Button 
              onClick={handleDownloadResume}
              className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
            >
              <Download className="w-4 h-4 mr-2" />
              Resume
            </Button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="pt-20">
        {/* Hero Section */}
        <section className="py-20 px-6">
          <div className="container mx-auto text-center">
            <div className="w-32 h-32 bg-gradient-to-r from-blue-600 to-purple-600 rounded-full mx-auto mb-8 flex items-center justify-center text-4xl font-bold">
              RK
            </div>
            <h1 className="text-5xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
              Solution Developer
            </h1>
            <p className="text-xl text-gray-300 mb-8 max-w-3xl mx-auto">
              Java-based middleware solutions, API development, and system integration specialist 
              with 2.5+ years of experience delivering scalable, secure, and business-aligned microservices.
            </p>
            <div className="flex items-center justify-center space-x-6 text-gray-400 mb-8">
              <div className="flex items-center space-x-2">
                <MapPin className="w-5 h-5" />
                <span>Tata Technologies</span>
              </div>
              <div className="flex items-center space-x-2">
                <Calendar className="w-5 h-5" />
                <span>2.5+ Years Experience</span>
              </div>
            </div>
            <div className="flex justify-center space-x-4">
              <Button 
                onClick={() => setActiveSection("projects")}
                className="bg-blue-600 hover:bg-blue-700"
              >
                View Projects
              </Button>
              <Button 
                onClick={() => setActiveSection("contact")}
                variant="outline"
                className="border-gray-600 text-gray-300 hover:bg-gray-800"
              >
                Contact Me
              </Button>
            </div>
          </div>
        </section>

        {/* Content Sections */}
        <div className="container mx-auto px-6 py-12">
          <Tabs value={activeSection} onValueChange={setActiveSection} className="w-full">
            <TabsList className="grid w-full grid-cols-5 bg-gray-900">
              <TabsTrigger value="about">About</TabsTrigger>
              <TabsTrigger value="projects">Projects</TabsTrigger>
              <TabsTrigger value="skills">Skills</TabsTrigger>
              <TabsTrigger value="achievements">Achievements</TabsTrigger>
              <TabsTrigger value="contact">Contact</TabsTrigger>
            </TabsList>

            {/* About Section */}
            <TabsContent value="about" className="mt-8">
              <Card className="bg-gray-900 border-gray-800">
                <CardHeader>
                  <CardTitle className="text-3xl text-white">About Me</CardTitle>
                </CardHeader>
                <CardContent className="text-gray-300 space-y-6">
                  <p className="text-lg leading-relaxed">
                    {mockData.about.description}
                  </p>
                  <div className="grid md:grid-cols-3 gap-6">
                    <div className="flex items-start space-x-3">
                      <Code className="w-6 h-6 text-blue-400 mt-1" />
                      <div>
                        <h3 className="font-semibold text-white mb-2">Backend Development</h3>
                        <p className="text-sm">Java, Spring Boot, Apache Camel, REST/SOAP services</p>
                      </div>
                    </div>
                    <div className="flex items-start space-x-3">
                      <Database className="w-6 h-6 text-purple-400 mt-1" />
                      <div>
                        <h3 className="font-semibold text-white mb-2">System Integration</h3>
                        <p className="text-sm">Middleware solutions, API development, microservices</p>
                      </div>
                    </div>
                    <div className="flex items-start space-x-3">
                      <Server className="w-6 h-6 text-green-400 mt-1" />
                      <div>
                        <h3 className="font-semibold text-white mb-2">Enterprise Solutions</h3>
                        <p className="text-sm">Scalable, secure, business-aligned systems</p>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </TabsContent>

            {/* Projects Section */}
            <TabsContent value="projects" className="mt-8">
              <div className="grid gap-6">
                {mockData.projects.map((project, index) => (
                  <Card key={index} className="bg-gray-900 border-gray-800 hover:border-blue-500 transition-all duration-300">
                    <CardHeader>
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-2xl text-white">{project.title}</CardTitle>
                        <ExternalLink className="w-5 h-5 text-gray-400" />
                      </div>
                    </CardHeader>
                    <CardContent>
                      <p className="text-gray-300 mb-4">{project.description}</p>
                      <div className="mb-4">
                        <h4 className="font-semibold text-white mb-2">Key Highlights:</h4>
                        <ul className="list-disc list-inside text-gray-300 space-y-1">
                          {project.highlights.map((highlight, i) => (
                            <li key={i}>{highlight}</li>
                          ))}
                        </ul>
                      </div>
                      <div className="flex flex-wrap gap-2">
                        {project.technologies.map((tech, i) => (
                          <Badge key={i} variant="secondary" className="bg-gray-800 text-gray-300">
                            {tech}
                          </Badge>
                        ))}
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </TabsContent>

            {/* Skills Section */}
            <TabsContent value="skills" className="mt-8">
              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                {mockData.skills.map((category, index) => (
                  <Card key={index} className="bg-gray-900 border-gray-800">
                    <CardHeader>
                      <CardTitle className="text-xl text-white">{category.category}</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="flex flex-wrap gap-2">
                        {category.items.map((skill, i) => (
                          <Badge key={i} variant="outline" className="border-gray-600 text-gray-300">
                            {skill}
                          </Badge>
                        ))}
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </TabsContent>

            {/* Achievements Section */}
            <TabsContent value="achievements" className="mt-8">
              <div className="grid gap-6">
                <Card className="bg-gray-900 border-gray-800">
                  <CardHeader>
                    <CardTitle className="text-2xl text-white flex items-center">
                      <Award className="w-6 h-6 mr-2 text-yellow-400" />
                      Professional Achievements
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      {mockData.achievements.map((achievement, index) => (
                        <div key={index} className="flex items-start space-x-3">
                          <div className="w-2 h-2 bg-blue-400 rounded-full mt-3"></div>
                          <div>
                            <h3 className="font-semibold text-white">{achievement.title}</h3>
                            <p className="text-gray-300">{achievement.description}</p>
                          </div>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>
                
                <Card className="bg-gray-900 border-gray-800">
                  <CardHeader>
                    <CardTitle className="text-2xl text-white">Certifications</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid md:grid-cols-2 gap-4">
                      {mockData.certifications.map((cert, index) => (
                        <div key={index} className="p-4 bg-gray-800 rounded-lg">
                          <h3 className="font-semibold text-white mb-1">{cert.name}</h3>
                          <p className="text-sm text-gray-400">{cert.issuer}</p>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              </div>
            </TabsContent>

            {/* Contact Section */}
            <TabsContent value="contact" className="mt-8">
              <Card className="bg-gray-900 border-gray-800">
                <CardHeader>
                  <CardTitle className="text-3xl text-white">Get In Touch</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="grid md:grid-cols-2 gap-8">
                    <div className="space-y-6">
                      <div className="flex items-center space-x-4">
                        <Mail className="w-6 h-6 text-blue-400" />
                        <div>
                          <p className="text-gray-300">Email</p>
                          <p className="text-white font-semibold">{mockData.contact.email}</p>
                        </div>
                      </div>
                      <div className="flex items-center space-x-4">
                        <Phone className="w-6 h-6 text-green-400" />
                        <div>
                          <p className="text-gray-300">Phone</p>
                          <p className="text-white font-semibold">{mockData.contact.phone}</p>
                        </div>
                      </div>
                      <div className="flex items-center space-x-4">
                        <Linkedin className="w-6 h-6 text-blue-500" />
                        <div>
                          <p className="text-gray-300">LinkedIn</p>
                          <p className="text-white font-semibold">{mockData.contact.linkedin}</p>
                        </div>
                      </div>
                    </div>
                    <div className="space-y-4">
                      <p className="text-gray-300">
                        I'm always open to discussing new opportunities and interesting projects. 
                        Feel free to reach out if you'd like to connect!
                      </p>
                      <div className="flex space-x-4">
                        <Button className="bg-blue-600 hover:bg-blue-700">
                          <Mail className="w-4 h-4 mr-2" />
                          Send Email
                        </Button>
                        <Button variant="outline" className="border-gray-600 text-gray-300 hover:bg-gray-800">
                          <Linkedin className="w-4 h-4 mr-2" />
                          LinkedIn
                        </Button>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </TabsContent>
          </Tabs>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-900 border-t border-gray-800 py-8">
        <div className="container mx-auto px-6 text-center">
          <p className="text-gray-400">
            © 2024 Riddhi Kalra. Built with passion for clean code and innovative solutions.
          </p>
        </div>
      </footer>
    </div>
  );
};

export default Portfolio;