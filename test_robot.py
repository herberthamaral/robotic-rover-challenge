from robot import robot

def test_rover_without_moves_should_do_nothing():
    position=[1,2,'N']
    final_position = robot(position=position, movements=[])
    assert position == final_position

def test_rover_facing_north_should_increment_y_by_one_when_moves():
    position=[1,2,'N']
    final_position = robot(position=position, movements=['M'])
    assert final_position == [1, 3, 'N']
