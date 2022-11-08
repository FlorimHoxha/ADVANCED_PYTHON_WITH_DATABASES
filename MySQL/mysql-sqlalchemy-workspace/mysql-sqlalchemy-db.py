from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqlconnector://root:mysqlpass@localhost:3306/household", echo=True)

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    __table_args__ = {'schema':'household'}

    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project(title'{0}', description='{1}'>".format(self.title, self.description)

class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema':'household'}

    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('household.projects.project_id'))
    description = Column(String(length=50))

    project = relationship("Project")

    def __repr__(self):
        return "<Task(description='{0}'>".format(self.description)

Base.metadata.create_all(engine)

session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

organise_closet_project = Project(title='Organised closet', description='Organised closet by colour and style')
session.add(organise_closet_project)
session.commit()

tasks = [Task(project_id=organise_closet_project.project_id, description='Decide what close to donate'),
         Task(project_id=organise_closet_project.project_id, description='Organise winter clothes'),
         Task(project_id=organise_closet_project.project_id, description='Organise summer clothes')]

session.bulk_save_objects(tasks)
session.commit()

our_project = session.query(Project).filter_by(title='Organise closet').first()
print(our_project)

our_tasks = session.query(Task).all()
print(our_tasks)
