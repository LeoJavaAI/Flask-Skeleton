#http://flask.pocoo.org/docs/0.10/testing/
#http://www.diveintopython3.net/unit-testing.html
#http://werkzeug.pocoo.org/docs/0.10/test/#testing-api

import unittest
from app import create_app
from app.users.models import Users

app = create_app('config')

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.add_success = False
        
    def test_list(self): 
      self.app = app.test_client()    
      rv = self.app.get('/users/')
      assert "Users" in rv.data.decode('utf-8')
      
             
    def test_add(self):
        rv = self.app.post('/users/add', data=dict(name = 'test name', email = 'test@email.com'), follow_redirects=True)
        self.add_success = True
        assert 'Add was successful' in rv.data.decode('utf-8')
    
     
    @unittest.skipUnless(self.add_success)        
    def test_Update(self):
         with app.app_context():
            id = Users.query.first().id
            rv = self.app.post('/users/update/{}'.format(id), data=dict(name = 'test name update', email = 'test@email.update'), follow_redirects=True)
            assert 'Update was successful' in rv.data.decode('utf-8')

    """def test_delete(self):
               
                    rv = self.app.post('/users/delete/{}'.format(id), follow_redirects=True)
                    assert 'Delete was successful' in rv.data.decode('utf-8')
        """
     
    
        
   
     
if __name__ == '__main__':
    unittest.main()
    
    
    
