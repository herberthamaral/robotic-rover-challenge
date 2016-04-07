from robot import robot

def test_rover_without_moves_should_do_nothing():
    position=[1,2,'N']
    final_position = robot(position=position, movements=[])
    assert position == final_position

def test_rover_facing_north_should_increment_y_by_one_when_it_moves():
    position=[1,2,'N']
    final_position = robot(position=position, movements=['M'])
    assert final_position == [1, 3, 'N']

def test_rover_facing_north_should_face_west_when_rotate_to_left():
    position=[1,2,'N']
    final_position = robot(position=position, movements=['L'])
    assert final_position == [1, 2, 'W']

def test_rover_facing_south_should_decrement_y_by_one_when_it_moves():
    position=[1,2,'S']
    final_position = robot(position=position, movements=['M'])
    assert final_position == [1, 1, 'S']

def test_rover_facing_east_should_increment_x_by_one_when_it_moves():
    position=[1,2,'E']
    final_position = robot(position=position, movements=['M'])
    assert final_position == [2, 2, 'E']

def test_rover_facing_west_should_decrement_x_by_one_when_it_moves():
    position=[1,2,'W']
    final_position = robot(position=position, movements=['M'])
    assert final_position == [0, 2, 'W']

def test_rover_facing_north_should_face_east_when_rotate_to_right():
    position=[1,2,'N']
    final_position = robot(position=position, movements=['R'])
    assert final_position == [1, 2, 'E']

def test_rover_facing_east_should_face_south_when_rotate_to_right():
    position=[1,2,'E']
    final_position = robot(position=position, movements=['R'])
    assert final_position == [1, 2, 'S']

def test_rover_facing_south_should_face_west_when_rotate_to_right():
    position=[1,2,'S']
    final_position = robot(position=position, movements=['R'])
    assert final_position == [1, 2, 'W']

def test_rover_facing_west_should_face_north_when_rotate_to_right():
    position=[1,2,'W']
    final_position = robot(position=position, movements=['R'])
    assert final_position == [1, 2, 'N']
