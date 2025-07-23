import { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from '@/context/AuthContext';

type Branch = {
  id: number;
  name: string;
  branch_code: string;
};

export function useBranches() {
  const [branches, setBranches] = useState<Branch[]>([]);
  const [filteredBranches, setFilteredBranches] = useState<Branch[]>([]);
  const [loading, setLoading] = useState(true);
  const { refreshToken } = useAuth();

  const filterBranches = (searchTerm: string) => {
    if (!searchTerm) {
      setFilteredBranches(branches);
      return;
    }
    const filtered = branches.filter(branch => 
      branch.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      branch.branch_code.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredBranches(filtered);
  };

  useEffect(() => {
    const fetchBranches = async () => {
      try {
        const response = await axios.get('/api/branches/');
        setBranches(response.data.branches);
      } catch (error) {
        if (axios.isAxiosError(error) && error.response?.status === 401) {
          await refreshToken();
          fetchBranches();
        }
      } finally {
        setLoading(false);
      }
    };

    fetchBranches();
  }, [refreshToken]);

  return { branches, filteredBranches, loading, filterBranches };
}
